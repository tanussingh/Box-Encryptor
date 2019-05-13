#   By: Tanushri Singh, Ko-Chen Chen, Lauren Murphy
#   CS 6348 - Data and Application Security
#   Instructor: Murat Kantarcioglu

"""boxIO.py
This provides all of the api calls to box that we will need
"""

#Import Libaries
from boxsdk import OAuth2, Client
import re

def boxUpload(client, path):
	"""Upload files to Box
	Params:	path - path to a file to be uploaded
			pubkeyid - download the public key file
	Return: box_file - object for the file
	"""
	file_info = []
	for x in path:
		box_file = client.folder(0).upload(x)
		file_info.append(box_file.id)
	return file_info

def boxSearch(client):
	""" Search Box for all files
	limits to 100 files
	Return:	files - an array of client.file objects
	"""
	files = []
	items_iter = client.folder(folder_id=0).get_items(limit=100, offset=0)
	for x in items_iter:
		files.append(x)
	return files

def boxDownload(client, file_ids):
	"""Download files
	Params:	file_ids - a array/list of files to download
	"""
	for i in file_ids:
		file = client.file(file_id=i).get()
		output_file = open(file.name, 'wb')
		file.download_to(output_file)
		output_file.close()

def boxShare(client, file_id, email):
	"""Share a file to email
	Params:	file_ids - a array of files to share
	"""
	for i in file_id:
		client.file(i).collaborate_with_login(email, role='VIEWER')

def boxUpdate(client, file_id, path):
	"""Update existing file on box
	Params: file_id - file to be updated
			path - path to new file
	Return: box_file - object for the file
	"""
	box_file = client.file(file_id).update_contents(path)
	return box_file

def boxGetLink(client, file_id):
	return client.file(file_id).get_shared_link_download_url(access=u'open')

#-------------TEST------------------
"""
client = getClient('5hktjn45wuj5rhqz5jgs7ecu61ohsta7', 
					'Dihuus9YOCnm13Ylf03UnihIgXkyfvy1', 
					'oAXe1xpxBX59WPfungMEPx8Q1FFcu1wv')
public_key_file_id = '450516904071';
choice = -1

#test_files = ['450785501449', '450760856460']

while (choice != '0'):
	choice = raw_input('1.Upload File; 2.Download File; 3.Share File; 0.Exit: ')

	if (choice == '1'):
		file_path = raw_input('Path to file: ')
		upload(file_path, public_key_file_id)
	elif (choice == '2'):
		fil = search()
		for i in range(0, len(fil)):
			print i, fil[i].name
		dlf = raw_input('Choose a file: ')
		download([fil[int(dlf)].id])
	elif (choice == '3'):
		fil = search()
		for i in range(0, len(fil)):
			print i, fil[i].name
		sf = raw_input('Choose a file: ')
		url = share([fil[int(sf)].id])
		print(url)
"""