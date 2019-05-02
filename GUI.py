#   By: Tanushri Singh, Ko-Chen Chen, Lauren Murphy
#   CS 6348 - Data and Application Security
#   Instructor: Murat Kantarcioglu

###################
#WHAT IT SHOULD DO:-
#This python file will be the Graphical User Interface for the project
###################

#Import Libaries
from tkinter import font
from tkinter import *
from boxIO import *

def authWindow():
    def login(event):
        #Upon click, Perfrom authentication using box 
        #If proper call optionWindow()
        global client 
        client = boxGetClient(inputUsername.get(), inputPassword.get(), inputDevTok.get())
        rootWindow.destroy()
        optionWindow()
    def exit(event):
        rootWindow.destroy()

    # Set up Auth Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('EncryptBox Login')
    rootWindow.geometry('700x350')
    rootWindow.resizable(0,0)
    title = Label(rootWindow, text = 'ENCRYPTBOX', bg = 'black', fg = 'white')
    title.config(font = ('verdana', 40))
    title.pack(fill=X)
    logoTitle = Label(rootWindow, text = 'Secure your files! Use Box Encrypter!', bg = 'black', fg = 'red')
    logoTitle.config(font = ('verdana', 25))
    logoTitle.pack(fill=X)

    #Username and Password Authentication
    pathUsername = Label(rootWindow, text = 'Username for Box: ', fg = 'black')
    pathUsername.config(font = ('Arial', 20))
    pathUsername.place(x = 100, y = 150)
    inputUsername = Entry(rootWindow)
    inputUsername.place(height = 40, width = 250, x = 350, y = 150)
    pathPassword = Label(rootWindow, text = 'Password for Box: ', fg = 'black')
    pathPassword.config(font = ('Arial', 20))
    pathPassword.place(x= 100, y = 200)
    inputPassword = Entry(rootWindow)
    inputPassword.place(height = 40, width = 250, x = 350, y = 200)
    pathDevTok = Label(rootWindow, text = 'Developer Token: ', fg = 'black')
    pathDevTok.config(font = ('Arial', 20))
    pathDevTok.place(x = 100, y = 250)
    inputDevTok = Entry(rootWindow)
    inputDevTok.place(height = 40, width = 250, x = 350, y = 250)
    btnSubmit = Button(text = 'Login', fg = 'black', font = ('verdana', 15))
    btnSubmit.place(height = 40, width = 250, x = 365, y = 300)
    btnSubmit.bind('<Button-1>', login)
    btnExit = Button(text = 'Exit', fg = 'black', font = ('verdana', 15))
    btnExit.place(height = 40, width = 250, x = 85, y = 300)
    btnExit.bind('<Button-1>', exit)

    rootWindow.mainloop()               #Ensures window constantly displays until closed

def optionWindow():
    def upload(event):
        rootWindow.destroy()
        uploadFiles()
    def download(event):
        rootWindow.destroy()
        downloadFiles()
    def share(event):
        rootWindow.destroy()
        shareFiles()
    def logout(event):
        rootWindow.destroy()
        authWindow()

    # Set up Options Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('Action')
    rootWindow.geometry('700x350')
    rootWindow.resizable(0,0)
    title = Label(rootWindow, text = 'ENCRYPTBOX', bg = 'black', fg = 'white')
    title.config(font = ('verdana', 40))
    title.pack(fill=X)
    optionTitle = Label(rootWindow, text = 'Action of Choice?', bg = 'black', fg = 'red')
    optionTitle.config(font = ('verdana', 25))
    optionTitle.pack(fill=X)

    #Provide the 3 option buttons
    btnUpload = Button(text = 'Upload Files', fg = 'black', font = ('verdana', 15))
    btnUpload.place(height = 40, width = 250, x = 225, y = 150)
    btnUpload.bind('<Button-1>', upload)
    btnDownload = Button(text = 'Download Files', fg = 'black', font = ('verdana', 15))
    btnDownload.place(height = 40, width = 250, x = 225, y = 200)
    btnDownload.bind('<Button-1>', download)
    btnShare = Button(text = 'Share Files', fg = 'black', font = ('verdana', 15))
    btnShare.place(height = 40, width = 250, x = 225, y = 250)
    btnShare.bind('<Button-1>', share)
    btnLogout = Button(text = 'Logout', fg = 'black', font = ('verdana', 15))
    btnLogout.place(height = 40, width = 250, x = 225, y = 300)
    btnLogout.bind('<Button-1>', logout)

    rootWindow.mainloop()

def uploadFiles():
    def upload(event):
        #After input call uploading script 
        boxUpload(client, inputFilePath.get(), '450516904071')
    def menu(event):
        rootWindow.destroy()
        optionWindow()

    # Set up Options Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('Upload')
    rootWindow.geometry('700x350')
    rootWindow.resizable(0,0)
    title = Label(rootWindow, text = 'ENCRYPTBOX', bg = 'black', fg = 'white')
    title.config(font = ('verdana', 40))
    title.pack(fill=X)
    uploadTitle = Label(rootWindow, text = 'Uploading Files', bg = 'black', fg = 'red')
    uploadTitle.config(font = ('verdana', 25))
    uploadTitle.pack(fill=X)

    #Name of File that is to be uploaded
    pathOfFile = Label(rootWindow, text = 'Path for file: ', fg = 'black')
    pathOfFile.config(font = ('Arial', 20))
    pathOfFile.place(x = 25, y = 150)
    inputFilePath = Entry(rootWindow)
    inputFilePath.place(height = 40, width = 300, x = 350, y = 150)
    pathPublicKey = Label(rootWindow, text = 'Path for Public Key File: ', fg = 'black')
    pathPublicKey.config(font = ('Arial', 20))
    pathPublicKey.place(x= 25, y = 200)
    inputPublicKey = Entry(rootWindow)
    inputPublicKey.place(height = 40, width = 300, x = 350, y = 200)
    btnUpload = Button(text = 'Upload', fg = 'black', font = ('verdana', 15))
    btnUpload.place(height = 40, width = 250, x = 350, y = 250)
    btnUpload.bind('<Button-1>', upload)
    btnMenu = Button(text = 'Menu', fg = 'black', font = ('verdana', 15))
    btnMenu.place(height = 40, width = 250, x = 350, y = 300)
    btnMenu.bind('<Button-1>', menu)

    rootWindow.mainloop()

def downloadFiles():
    def download(event):
        #After input has been entered call downlaod script
        items = map(lambda x: files[x].id, listbox.curselection())
        boxDownload(client, items)
    def menu(event):
        rootWindow.destroy()
        optionWindow()

    # Set up Options Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('Download')
    rootWindow.geometry('700x350')
    rootWindow.resizable(0,0)
    title = Label(rootWindow, text = 'ENCRYPTBOX', bg = 'black', fg = 'white')
    title.config(font = ('verdana', 40))
    title.pack(fill=X)
    downloadTitle = Label(rootWindow, text = 'Downloading Files', bg = 'black', fg = 'red')
    downloadTitle.config(font = ('verdana', 25))
    downloadTitle.pack(fill=X)

    #get files currently in box
    files = boxSearch(client)

    listbox = Listbox(rootWindow, selectmode=MULTIPLE)
    listbox.place(height = 230, width = 300, x = 25, y = 115)
    for x in range(0, len(files)):
        listbox.insert(END, files[x].name)

    instLabel = Label(rootWindow, text = '<-Select all files to download', fg = 'black')
    instLabel.config(font = ('Arial', 20))
    instLabel.place(x = 350, y = 150)
    btnDownload = Button(text = 'Download', fg = 'black', font = ('verdana', 15))
    btnDownload.place(height = 40, width = 250, x = 350, y = 200)
    btnDownload.bind('<Button-1>', download)
    btnMenu = Button(text = 'Menu', fg = 'black', font = ('verdana', 15))
    btnMenu.place(height = 40, width = 250, x = 350, y = 250)
    btnMenu.bind('<Button-1>', menu)

    rootWindow.mainloop()

def shareFiles():
    def share(event):
        def close(event):
            subWindow.destroy()
        #After input call sharing script
        subWindow = Tk()
        subWindow.title('Links to Share')
        subWindow.geometry('550x250')
        subWindow.resizable(0,0)

        items = map(lambda x: files[x].id, listbox.curselection())
        urls = boxShare(client, items)

        linksListBox = Listbox(subWindow, selectmode=MULTIPLE)
        linksListBox.pack(fill=X)
        for x in range(0, len(urls)):
            linksListBox.insert(END, urls[x])

        btnClose = Button(subWindow, text = 'Close', fg = 'black', font = ('verdana', 15))
        btnClose.place(height = 40, width = 250, x = 300, y = 200)
        btnClose.bind('<Button-1>', close)

        subWindow.mainloop()
    def menu(event):
        rootWindow.destroy()
        optionWindow()
    # Set up Options Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('Share')
    rootWindow.geometry('700x350')
    rootWindow.resizable(0,0)
    title = Label(rootWindow, text = 'ENCRYPTBOX', bg = 'black', fg = 'white')
    title.config(font = ('verdana', 40))
    title.pack(fill=X)
    shareTitle = Label(rootWindow, text = 'Sharing Files', bg = 'black', fg = 'red')
    shareTitle.config(font = ('verdana', 25))
    shareTitle.pack(fill=X)

    #get files currently in box
    files = boxSearch(client)

    listbox = Listbox(rootWindow, selectmode=MULTIPLE)
    listbox.place(height = 230, width = 300, x = 25, y = 115)
    for x in range(0, len(files)):
        listbox.insert(END, files[x].name)
    
    instLabel = Label(rootWindow, text = '<-Select all files to share', fg = 'black')
    instLabel.config(font = ('Arial', 20))
    instLabel.place(x = 350, y = 150)
    btnShare = Button(text = 'Share', fg = 'black', font = ('verdana', 15))
    btnShare.place(height = 40, width = 250, x = 350, y = 200)
    btnShare.bind('<Button-1>', share)
    btnMenu = Button(text = 'Menu', fg = 'black', font = ('verdana', 15))
    btnMenu.place(height = 40, width = 250, x = 350, y = 250)
    btnMenu.bind('<Button-1>', menu)
    
    rootWindow.mainloop()

authWindow()

