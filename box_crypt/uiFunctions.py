from file import *
from box import *
import urllib.request
import csv
from crypto import *
from box import *

def uiShare(client, collab, filename):
    #variable
    url = None
    found = False
    username = client.user(user_id='me').get().login

    sharer_key = read_user_private_key(username)

    boxDownload(client, ['456159607978'])
    with open('pub_key_list.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (row[0] == collab):
                url = row[1]
                found = True
    csv_file.close()

    if (not found):
        print ("Problem")
        #dead

    response = urllib.request.urlopen(url)
    data = response.read()
    #text = data.decode('utf-8')
    
    sharee_key = UserKey.deserialize_public(data)

    ### CHECK WHETHER FILE TO SHARE HAS ALREADY BEEN PUT ON BOX

    file_on_box = False

    files_on_box = boxSearch(client)

    file_to_reshare = None

    for file in files_on_box:
        if file.name == get_encrypted_filename(filename):
            file_on_box = True
            file_to_reshare = file.id

    ## WE DO IT

    if file_on_box:
        print("File already on box")

        box_search = boxSearch(client)
        my_file_key_file_id = None

        for file in box_search:
            if file.name == get_file_key_filename(filename, client.user(user_id='me').get().login):
                my_file_key_file_id = file.id

        boxDownload(client, [my_file_key_file_id])

        file_key = read_file_key(filename,
            client.user(user_id='me').get().login,
            sharer_key,
            sharer_key)

        write_file_key(filename, collab, file_key, sharee_key, sharer_key)

        fileinfos = boxUpload(client, [
            get_file_key_filename(filename, collab)
        ])

        fileinfos.append(file_to_reshare)

        boxShare(client, fileinfos, collab)

    else:
        file_key = FileKey.generate()

        write_encrypted_file(filename, file_key, read_unencrypted_file(filename))

        write_file_key(filename, collab, file_key, sharee_key, sharer_key)

        # Mine for future use
        write_file_key(filename, client.user(user_id='me').get().login, file_key, sharer_key, sharer_key)

        fileinfos = boxUpload(client, [
            get_encrypted_filename(filename),
            get_file_key_filename(filename, collab),
            get_file_key_filename(filename, client.user(user_id='me').get().login)
        ])

        boxShare(client, fileinfos, collab)

def uiView(client, sharer, filename, ids):
    #variable
    url = None
    found = False
    file_id = []
    username = client.user(user_id='me').get().login

    boxDownload(client, ['456159607978'])
    with open('pub_key_list.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (row[0] == sharer):
                url = row[1]
                found = True
    csv_file.close()

    if (not found):
        print ("Problem")
        #dead

    response = urllib.request.urlopen(url)
    data = response.read()

    for i in ids:
        if (filename in i.name):
            file_id.append(i.id)

    boxDownload(client, file_id)

    sharee_key = read_user_private_key(username)

    sharer_key = UserKey.deserialize_public(data)

    file_key = read_file_key(filename, username, sharee_key, sharer_key)

    write_unencrypted_file(filename, read_encrypted_file(filename, file_key))

