from crypto import *


def get_encrypted_filename(filename):
    return filename + ".bc"


def get_file_key_filename(filename, sharee_username):
    return filename + ".u." + sharee_username + ".fk"


def get_user_key_filename(username, isSecret):
    return username + "." + ("sk" if isSecret else "pk") + ".pem"


def write_user_private_key(username, private_key):
    write(
        get_user_key_filename(username, True),
        private_key.serialize_private()
    )


def write_user_public_key(username, public_key):
    write(
        get_user_key_filename(username, False),
        public_key.serialize_public()
    )


def write_file_key(filename, sharee_username, file_key, sharee_public_key, sharer_key):
    write(
        get_file_key_filename(filename, sharee_username),
        file_key.serialize(
            sharee_public_key=sharee_public_key,
            sharer_key=sharer_key
        )
    )


def write_unencrypted_file(filename, contents):
    write(filename, contents)


def write_encrypted_file(filename, file_key, contents):
    write(get_encrypted_filename(filename), file_key.encrypt(contents))


def read_user_private_key(username):
    return UserKey.deserialize_private(
        read(get_user_key_filename(username, True))
    )


def read_user_public_key(username):
    return UserKey.deserialize_public(
        read(get_user_key_filename(username, False))
    )


def read_file_key(filename, sharee_username, sharee_key, sharer_public_key):
    return FileKey.deserialize(
        serialized=read(get_file_key_filename(filename, sharee_username)),
        sharee_key=sharee_key,
        sharer_public_key=sharer_public_key
    )


def read_unencrypted_file(filename):
    return read(filename)


def read_encrypted_file(filename, file_key):
    return file_key.decrypt(
        read(get_encrypted_filename(filename))
    )


def read(path):
    file = open(path, "rb")
    contents = file.read()
    file.close()
    return contents


def write(path, contents):
    file = open(path, "wb+")
    file.write(contents)
    file.close()
