#curl https://api.box.com/2.0/folders/0 -H \
#"Authorization: Bearer 5WJNW4wrXpXCVaDeOQo4aGpl7fI4IlQB"

from boxsdk import OAuth2, Client

def upload(path, pubkeyid):
	#download pubkey
	download(pubkeyid)
	#send path of file to be encrypted to encrypted
	#get path to two files back
	#upload two files
	#box_file = client.folder(0).upload(path)
	box_file = client.folder(0).upload(path)

def search():
	files = []

	items_iter = client.folder(folder_id=0).get_items(limit=100, offset=0)

	for x in items_iter:
		files.append(x)

	return files

def download(file_id):
	if (file_id == public_key_file_id):
		file = client.file(file_id=file_id).get()
		output_file = open(file.name, 'wb')
		file.download_to(output_file)
		output_file.close()
	else:
		#need to download two files if not public key
		print("end here")
	

def share(file_id):
	file = client.file(file_id);
	return file.get_shared_link_download_url(access=u'open')

#-------------MAIN------------------
auth = OAuth2(
    client_id='5hktjn45wuj5rhqz5jgs7ecu61ohsta7',
    client_secret='Dihuus9YOCnm13Ylf03UnihIgXkyfvy1',
    access_token='Bu4iAOSsdtgU4XsJXT6egOythNWpAbKv',
)
client = Client(auth)
public_key_file_id = '450516904071';
choice = -1

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
		download(fil[int(dlf)].id)
	elif (choice == '3'):
		fil = search()
		for i in range(0, len(fil)):
			print i, fil[i].name
		sf = raw_input('Choose a file: ')
		url = share(fil[int(sf)].id)
		print(url)