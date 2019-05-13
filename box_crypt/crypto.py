import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

from misc import *


# Asymmetric key associated with a user
# Used for encrypting / decrypting and signing / verifying file key to share with user
class UserKey:

    GENERATED_KEY_SIZE = 4096  # Default.

    ENCRYPT_PADDING = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )

    SIGN_PADDING = padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    )

    # Given private key, it can infer public key (vice-versa is NOT true)
    def __init__(self, private=None, public=None):
        self.private = private
        self.public = public

        if private is not None and public is None:
            self.public = private.public_key()

    # (Requires public key)
    def encrypt(self, plaintext):
        return self.public.encrypt(plaintext, UserKey.ENCRYPT_PADDING)

    # (Requires private key)
    def decrypt(self, ciphertext):
        return self.private.decrypt(ciphertext, UserKey.ENCRYPT_PADDING)

    # (Requires private key)
    def sign(self, text):
        return self.private.sign(
            data=text,
            padding=UserKey.SIGN_PADDING,
            algorithm=hashes.SHA256()
        )

    # (Requires public key)
    def verify(self, text, signature):
        return self.public.verify(
            signature=signature,
            data=text,
            padding=UserKey.SIGN_PADDING,
            algorithm=hashes.SHA256()
        )

    @staticmethod
    def generate():
        private = rsa.generate_private_key(
            public_exponent=65537,
            key_size=UserKey.GENERATED_KEY_SIZE,
            backend=default_backend()
        )

        return UserKey(private=private, public=private.public_key())

    def serialize_private(self):
        return self.private.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

    @staticmethod
    def deserialize_private(serialized_private):
        private = serialization.load_pem_private_key(
            serialized_private,
            password=None,
            backend=default_backend()
        )

        return UserKey(private=private)

    def serialize_public(self):
        return self.public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    @staticmethod
    def deserialize_public(serialized_public):
        public = serialization.load_pem_public_key(
            serialized_public,
            backend=default_backend()
        )

        return UserKey(public=public)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


# Symmetric key associated with file
# Used for encrypting / decrypting file
class FileKey:

    GENERATED_KEY_SIZE = 256  # Default.

    DELIMITER = b'*******'

    def __init__(self, key=None, nonce=None):
        self.key = key
        self.nonce = nonce

    def encrypt(self, unencrypted):
        return AESGCM(self.key).encrypt(self.nonce, unencrypted, None)

    def decrypt(self, encrypted):
        return AESGCM(self.key).decrypt(self.nonce, encrypted, None)

    # Returns bytes to write out to file
    # sharee_public_key is a UserKey object with only sharee's public key
    # sharer_key is a UserKey object with sharer's private key
    #
    # We encrypt key, then get signature for the encrypted key
    #
    # Put signature, ******* (7 *), then encrypted file in byte array
    def serialize(self, sharee_public_key, sharer_key):
        # Encode key and nonce to Base64 as bytes, then convert bytes to string for dictionary
        key = encode(self.key).decode('utf-8')
        nonce = encode(self.nonce).decode('utf-8')

        dictionary = {'key':  key, 'nonce':  nonce}

        # Convert dictionary to JSON as string then convert string to bytes
        unencrypted = bytes(dict_to_json(dictionary), 'utf-8')

        encrypted = sharee_public_key.encrypt(unencrypted)
        signature = sharer_key.sign(encrypted)

        serialized = signature + FileKey.DELIMITER + encrypted

        return serialized

    # Pass bytes from file
    # Returns FileKey object
    # sharee_key is UserKey object with sharee's private key
    # sharer_public_key is UserKey object with only sharer's public key
    @staticmethod
    def deserialize(serialized, sharee_key, sharer_public_key):
        split = serialized.split(FileKey.DELIMITER)
        signature = split[0]
        encrypted = split[1]

        sharer_public_key.verify(text=encrypted, signature=signature)

        decrypted = sharee_key.decrypt(encrypted)

        # Convert JSON as string to dictionary
        dictionary = json_to_dict(decrypted)

        # Decode key and nonce from Base64 as strings to bytes
        key = decode(dictionary['key'])
        nonce = decode(dictionary['nonce'])

        return FileKey(key=key, nonce=nonce)

    @staticmethod
    def generate():
        return FileKey(key=AESGCM.generate_key(bit_length=FileKey.GENERATED_KEY_SIZE), nonce=os.urandom(12))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
