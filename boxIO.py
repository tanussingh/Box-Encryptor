#   By: Tanushri Singh, Ko-Chen Chen, Lauren Murphy
#   CS 6348 - Data and Application Security
#   Instructor: Murat Kantarcioglu

"""boxIO.py
This provides all of the api calls to box that we will need
"""

#Import Libaries
from boxsdk import OAuth2, Client

def getClient(id, secret, access_token):
	"""creates the OAuth2 object for box client
	Input:	id - client/app id
			secret - client/app secret
			access_token - developer token
	Return:	Client(oAuth2) - Box client object
	"""
	oAuth2 = OAuth2(
	    client_id = id,
	    client_secret = secret,
	    access_token = access_token,
	)
	return Client(oAuth2)


def upload(client, path, pubkeyid):
	"""Upload files to Box
	Params:	path - path to a file to be uploaded
			pubkeyid - download the public key file
	"""
	#download pubkey
	download(pubkeyid)
	#send path of file to be encrypted to encrypted
	#get path to two files back
	#upload two files
	#box_file = client.folder(0).upload(path)
	box_file = client.folder(0).upload(path)

def search(client):
	""" Search Box for all files
	limits to 100 files
	Return:	files - an array of client.file objects
	"""
	files = []
	items_iter = client.folder(folder_id=0).get_items(limit=100, offset=0)
	for x in items_iter:
		files.append(x)
	return files

def download(client, file_ids):
	"""Download files
	Params:	file_ids - a array/list of files to download
	"""
	for i in file_ids:
		file = client.file(file_id=i).get()
		output_file = open(file.name, 'wb')
		file.download_to(output_file)
		output_file.close()

def share(client, file_ids):
	"""Get sharable link for a file
	Params:	file_ids - a array/list of files to download
	Return:	urls - an array of strings
	"""
	urls = []
	for i in file_ids:
		urls.append(client.file(file_id=i).get_shared_link_download_url(access=u'open'))
	return urls

#-------------TEST------------------
"""
client = getClient('5hktjn45wuj5rhqz5jgs7ecu61ohsta7', 'Dihuus9YOCnm13Ylf03UnihIgXkyfvy1', 'ZsBMXPv4cNaDbOnRIMI9O5fiaMAbIV0K')
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