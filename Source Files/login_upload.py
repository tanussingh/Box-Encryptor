#curl https://api.box.com/2.0/folders/0 -H \
#"Authorization: Bearer 5WJNW4wrXpXCVaDeOQo4aGpl7fI4IlQB"

from boxsdk import OAuth2, Client

def upload(path):
	box_file = client.folder(0).upload(path)

def search():
	item_names = []
	item_ids = []

	items_iter = client.folder(folder_id=0).get_items(limit=20, offset=0)

	for x in items_iter:
		item_names.append(x.name)
		item_ids.append(x.id)

	return item_names, item_ids

def download(file_id):
	file = client.file(file_id=file_id).get()
	output_file = open(file.name, 'wb')
	file.download_to(output_file)

def getSharedLink(file_id, access_level):
	file = client.file(file_id);
	return file.get_shared_link(access=access_level)

#-------------MAIN------------------
auth = OAuth2(
    client_id='5hktjn45wuj5rhqz5jgs7ecu61ohsta7',
    client_secret='Dihuus9YOCnm13Ylf03UnihIgXkyfvy1',
    access_token='elfRf8X7hGNlbVGwnfe2XZdzckEMRrW9',
)
client = Client(auth)

choice = -1

while (choice != '0'):
	choice = raw_input('1.Upload File; 2.Download File; 0.Exit: ')

	if (choice == '1'):
		file_path = raw_input('Path to file: ')
		upload(file_path)
	elif (choice == '2'):
		names, ids = search();
		print(names)
		dlf = raw_input('Choose a file (0 for first file, 1 for second, etc): ')
		download(ids[int(dlf)])