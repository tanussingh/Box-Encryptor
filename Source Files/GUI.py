#   By: Tanushri Singh, Jack Chen, Lauren Murphy
#   CS 6348 - Data and Application Security
#   Instructor: Murat Kantarcioglu

###################
#WHAT IT SHOULD DO:-
#This python file will be the Graphical User Interface for the project
###################

#Import Libaries
from tkinter import *

class GUI:
    def authWindow():
        # Set up Auth Frame
        rootWindow = Tk()                   #Constructor rootWindow - main window
        rootWindow.title('EncryptBox Login')
        rootWindow.geometry("550x320")
        rootWindow.resizable(0,0)
        title = Label(rootWindow, text = "ENCRYPTBOX", bg = "black", fg = "white")
        title.config(font = ("verdana", 40))
        title.pack(fill=X)
        logoTitle = Label(rootWindow, text = "Secure your files! Use Box Encrypter!", bg = "black", fg = "red")
        logoTitle.config(font = ("verdana", 25))
        logoTitle.pack(fill=X)

        #Username and Password Authentication
        pathUsername = Label(rootWindow, text = "Username for Box: ", fg = "black")
        pathUsername.config(font = ("Arial", 20))
        pathUsername.place(x = 25, y = 100)
        inputUsername = Entry(rootWindow)
        inputUsername.place(height = 40, width = 150, x = 300, y = 100)
        pathPassword = Label(rootWindow, text = "Password for Box: ", fg = "black")
        pathPassword.config(font = ("Arial", 20))
        pathPassword.place(x= 25, y = 150)
        inputPassword = Entry(rootWindow)
        inputPassword.place(height = 40, width = 150, x = 300, y = 150)
        pathDevTok = Label(rootWindow, text = "Enter Developer Token: ", fg = "black")
        pathDevTok.config(font = ("Arial", 20))
        pathDevTok.place(x = 25, y = 200)
        inputDevTok = Entry(rootWindow)
        inputDevTok.place(height = 40, width = 150, x = 300, y = 200)
        submitAuth = Button(text = "Login", fg = "black")
        submitAuth.place(height = 40, width = 250, x = 150, y = 250)

        rootWindow.mainloop()               #Ensures window constantly displays until closed

    def optionWindow():
        # Set up Options Frame
        rootWindow = Tk()                   #Constructor rootWindow - main window
        rootWindow.title('Action')
        rootWindow.geometry("550x320")
        rootWindow.resizable(0,0)
        title = Label(rootWindow, text = "ENCRYPTBOX", bg = "black", fg = "white")
        title.config(font = ("verdana", 40))
        title.pack(fill=X)
        optionTitle = Label(rootWindow, text = "What would you like to conduct today?", bg = "black", fg = "red")
        optionTitle.config(font = ("verdana", 25))
        optionTitle.pack(fill=X)

        #Provide the 3 option buttons
        submitAuth = Button(text = "Upload Files", fg = "black")
        submitAuth.place(height = 40, width = 250, x = 150, y = 100)
        submitAuth = Button(text = "Download Files", fg = "black")
        submitAuth.place(height = 40, width = 250, x = 150, y = 175)
        submitAuth = Button(text = "Share Files", fg = "black")
        submitAuth.place(height = 40, width = 250, x = 150, y = 250)

        rootWindow.mainloop()

    def uploadFiles():
        # Set up Options Frame
        rootWindow = Tk()                   #Constructor rootWindow - main window
        rootWindow.title('Upload')
        rootWindow.geometry("550x320")
        rootWindow.resizable(0,0)
        title = Label(rootWindow, text = "ENCRYPTBOX", bg = "black", fg = "white")
        title.config(font = ("verdana", 40))
        title.pack(fill=X)
        uploadTitle = Label(rootWindow, text = "Uploading Files", bg = "black", fg = "red")
        uploadTitle.config(font = ("verdana", 25))
        uploadTitle.pack(fill=X)

    def downloadFiles():
        # Set up Options Frame
        rootWindow = Tk()                   #Constructor rootWindow - main window
        rootWindow.title('Download')
        rootWindow.geometry("550x320")
        rootWindow.resizable(0,0)
        title = Label(rootWindow, text = "ENCRYPTBOX", bg = "black", fg = "white")
        title.config(font = ("verdana", 40))
        title.pack(fill=X)
        downloadTitle = Label(rootWindow, text = "Downloading Files", bg = "black", fg = "red")
        downloadTitle.config(font = ("verdana", 25))
        downloadTitle.pack(fill=X)

    def shareFiles():
        # Set up Options Frame
        rootWindow = Tk()                   #Constructor rootWindow - main window
        rootWindow.title('Share')
        rootWindow.geometry("550x320")
        rootWindow.resizable(0,0)
        title = Label(rootWindow, text = "ENCRYPTBOX", bg = "black", fg = "white")
        title.config(font = ("verdana", 40))
        title.pack(fill=X)
        shareTitle = Label(rootWindow, text = "Sharing Files", bg = "black", fg = "red")
        shareTitle.config(font = ("verdana", 25))
        shareTitle.pack(fill=X)

    authWindow()
    optionWindow()
    uploadFiles()
    downloadFiles()
    shareFiles()
