#   By: Tanushri Singh
#   Teammates:- Jack Chen, Lauren Murphy
#   CS 6348 - Data and Application Security
#   Instructor: Murat Kantarcioglu

###################
#WHAT IT SHOULD DO:-
#This python file will be the Graphical User Interface for the project
###################

#Import Libaries
from tkinter import *

class GUI:
    def window():
        rootWindow = Tk()                   #Constructor rootWindow - main window
        rootWindow.geometry("550x400")
        title = Label(rootWindow, text = "ENCRYPTBOX", bg = "black", fg = "white")
        title.config(font = ("verdana", 40))
        title.pack(fill=X)
        citiesTitle = Label(rootWindow, text = "Secure your files! Use DropBox Encrypter!", bg = "black", fg = "red")
        citiesTitle.config(font = ("verdana", 25))
        citiesTitle.pack(fill=X)

        pathLabel = Label(rootWindow, text = "Provide path of the file to be encrypted: ", fg = "black")
        pathLabel.config(font = ("Arial", 20))
        pathLabel.place(x = 15, y = 100)
        inputDate = Entry(rootWindow)
        inputDate.place(height = 40, width = 230, x = 20, y = 140)

        submit = Button(text = "Submit", fg = "black")

        #Display the buttons:-
        submit.place(height = 40 , width = 150, x = 260, y = 140)

        rootWindow.mainloop()               #Ensures window constantly displays until closed

    window()
