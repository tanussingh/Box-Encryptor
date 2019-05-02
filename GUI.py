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
    def submitHandler(event):
        #Upon click, Perfrom authentication using box 
        #If proper call optionWindow()
        client = getClient(inputUsername.get(), inputPassword.get(), inputDevTok.get())
        rootWindow.destroy()
        optionWindow()
    # Set up Auth Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('EncryptBox Login')
    rootWindow.geometry('550x320')
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
    pathUsername.place(x = 25, y = 100)
    inputUsername = Entry(rootWindow)
    inputUsername.place(height = 40, width = 150, x = 300, y = 100)
    pathPassword = Label(rootWindow, text = 'Password for Box: ', fg = 'black')
    pathPassword.config(font = ('Arial', 20))
    pathPassword.place(x= 25, y = 150)
    inputPassword = Entry(rootWindow)
    inputPassword.place(height = 40, width = 150, x = 300, y = 150)
    pathDevTok = Label(rootWindow, text = 'Enter Developer Token: ', fg = 'black')
    pathDevTok.config(font = ('Arial', 20))
    pathDevTok.place(x = 25, y = 200)
    inputDevTok = Entry(rootWindow)
    inputDevTok.place(height = 40, width = 150, x = 300, y = 200)
    submitAuth = Button(text = 'Login', fg = 'black')
    submitAuth.place(height = 40, width = 250, x = 150, y = 250)
    submitAuth.bind('<Button-1>', submitHandler)

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

    # Set up Options Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('Action')
    rootWindow.geometry('550x320')
    rootWindow.resizable(0,0)
    title = Label(rootWindow, text = 'ENCRYPTBOX', bg = 'black', fg = 'white')
    title.config(font = ('verdana', 40))
    title.pack(fill=X)
    optionTitle = Label(rootWindow, text = 'Action of Choice?', bg = 'black', fg = 'red')
    optionTitle.config(font = ('verdana', 25))
    optionTitle.pack(fill=X)

    #Provide the 3 option buttons
    helv36 = font.Font(family='Helvetica', size=24)
    btnUpload = Button(text = 'Upload Files', fg = 'black', font=helv36)
    btnUpload.place(height = 40, width = 250, x = 150, y = 100)
    btnUpload.bind('<Button-1>', upload)
    btnDownload = Button(text = 'Download Files', fg = 'black', font=helv36)
    btnDownload.place(height = 40, width = 250, x = 150, y = 175)
    btnDownload.bind('<Button-1>', download)
    btnShare = Button(text = 'Share Files', fg = 'black', font=helv36)
    btnShare.place(height = 40, width = 250, x = 150, y = 250)
    btnShare.bind('<Button-1>', share)

    rootWindow.mainloop()

def uploadFiles():
    # Set up Options Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('Upload')
    rootWindow.geometry('600x320')
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
    pathOfFile.place(x = 25, y = 100)
    inputFilePath = Entry(rootWindow)
    inputFilePath.place(height = 40, width = 300, x = 280, y = 100)
    pathPublicKey = Label(rootWindow, text = 'Path for Public Key File: ', fg = 'black')
    pathPublicKey.config(font = ('Arial', 20))
    pathPublicKey.place(x= 25, y = 150)
    inputPublicKey = Entry(rootWindow)
    inputPublicKey.place(height = 40, width = 300, x = 280, y = 150)

    #After input call uploading script 

    rootWindow.mainloop()

def downloadFiles():
    # Set up Options Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('Download')
    rootWindow.geometry('600x320')
    rootWindow.resizable(0,0)
    title = Label(rootWindow, text = 'ENCRYPTBOX', bg = 'black', fg = 'white')
    title.config(font = ('verdana', 40))
    title.pack(fill=X)
    downloadTitle = Label(rootWindow, text = 'Downloading Files', bg = 'black', fg = 'red')
    downloadTitle.config(font = ('verdana', 25))
    downloadTitle.pack(fill=X)

    #Name of File that is to be downloaded
    pathOfFile = Label(rootWindow, text = 'Name of file: ', fg = 'black')
    pathOfFile.config(font = ('Arial', 20))
    pathOfFile.place(x = 25, y = 100)
    inputFileName = Entry(rootWindow)
    inputFileName.place(height = 40, width = 300, x = 280, y = 100)
    pathPublicKey = Label(rootWindow, text = 'Path for Public Key File: ', fg = 'black')
    pathPublicKey.config(font = ('Arial', 20))
    pathPublicKey.place(x= 25, y = 150)
    inputPublicKey = Entry(rootWindow)
    inputPublicKey.place(height = 40, width = 300, x = 280, y = 150)

    #After input has been entered call downlaod script

    rootWindow.mainloop()

def shareFiles():
    # Set up Options Frame
    rootWindow = Tk()                   #Constructor rootWindow - main window
    rootWindow.title('Share')
    rootWindow.geometry('600x200')
    rootWindow.resizable(0,0)
    title = Label(rootWindow, text = 'ENCRYPTBOX', bg = 'black', fg = 'white')
    title.config(font = ('verdana', 40))
    title.pack(fill=X)
    shareTitle = Label(rootWindow, text = 'Sharing Files', bg = 'black', fg = 'red')
    shareTitle.config(font = ('verdana', 25))
    shareTitle.pack(fill=X)

    #Name of File that is to be downloaded
    pathOfFile = Label(rootWindow, text = 'Name of file: ', fg = 'black')
    pathOfFile.config(font = ('Arial', 20))
    pathOfFile.place(x = 25, y = 100)
    inputFileName = Entry(rootWindow)
    inputFileName.place(height = 40, width = 300, x = 280, y = 100)
    pathOfUrl = Label(rootWindow, text = 'URL Link: ', fg = 'black')
    pathOfUrl.config(font = ('Arial', 20))
    pathOfUrl.place(x = 25, y = 150)

    #After input call sharing script 
    
    rootWindow.mainloop()


authWindow()

