from file import *
from box import *
import csv

client = None
sharer_username = None
pub_key_fileid = "456159607978"

# (Registering sharer)
def generate_key_pair():
    # Generate user keys
    sharer = UserKey.generate()

    # Write out user keys
    write_user_private_key(sharer_username, sharer)
    write_user_public_key(sharer_username, sharer)

def update_publist_file_and_upload(link):
    append = [sharer_username, link]
    with open('pub_key_list.txt', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(append)
    csv_file.close()
    boxUpdate(client, pub_key_fileid, 'pub_key_list.txt')

def start(cli):
    #set client
    global client
    client = cli

    #set username
    my = client.user(user_id='me').get()
    global sharer_username
    sharer_username = my.login

    #variables
    found = False

    #need to download public key list
    boxDownload(client, [pub_key_fileid])

    #check if ald have pub key
    with open('pub_key_list.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (row[0] == sharer_username):
                found = True
    csv_file.close()

    #if not create key
    if (not found):
        generate_key_pair()
        fileinfo = boxUpload(client, [sharer_username + '.pk.pem'])
        link = boxGetLink(client, fileinfo[0])
        update_publist_file_and_upload(link)
