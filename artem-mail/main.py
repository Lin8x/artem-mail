#!/usr/bin/python3

import os
from tkinter import *
from PIL import Image, ImageTk

# from pillow import Image, ImageTk

t = Tk()  # where m is the name of the main window object


def topbar():
    # top bar here
    image = Image.open("topbar.jpg")
    image = image.resize((500, 20), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo  # keep a reference!
    label.pack()


def opengithub():
    os.system("open https://github.com/Lin8x/artem-mail")


def startup():
    t.title("Artem Mail Tool")  # title of the tool
    t.geometry("500x400")  # Size of window
    TITLE_FONT = ("Helvetica", 18, "bold")  # The font of words

    # A frane is a rectangular region on the screen
    frame = Frame(t)
    # frame.pack()
    bottomframe = Frame(t)
    bottomframe.pack(side=BOTTOM)

    # A Canvas is used to draw pictures and other complex layout like graphics, text and widgets.
    c = Canvas(t, width=0, height=0)
    # c.pack()
    canvas_height = 20
    canvas_width = 200

    loginpage()


def loginpage():
    menu = Menu(t)
    # only help top menu bar for login screen    
    helpmenu = Menu(menu)
    helpmenu.add_command(label='About / Github Page', command=opengithub)
    helpmenu.add_command(label='Tool Documentation')
    helpmenu.add_command(label='Report Bugs/Glitches/Issues')
    menu.add_cascade(label='Help', menu=helpmenu)
    t.config(menu=menu)
    

    # logo here
    image = Image.open("artemlogo.png") # u need PNG file to store image Alpha
    image = image.resize((200, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo  # keep a reference!
    label.pack()

    # Everything below here is the buttons

    # Entry/Text Input
    label1 = Label(t, text="Gmail Username")
    E1 = Entry(t, bd=5, relief=GROOVE)

    label2 = Label(t, text="Gmail Password")
    E2 = Entry(t, bd=5, relief=GROOVE)

    label1.pack()
    E1.pack()
    label2.pack()
    E2.pack()

    # Button to quit the tool
    button2 = Button(t, text='Quit The Tool', width=20, bd=3,command=t.destroy)
    button1 = Button(t, text='Enter', width=20,bd=3,
                     command=lambda: logindestroy(label, label1, label2, E1, E2, button1, button2))
    button1.pack()
    button2.pack()


def logindestroy(label, label1, label2, E1, E2, button1, button2):
    label.destroy()
    label1.destroy()
    E1.destroy()
    label2.destroy()
    E2.destroy()
    button1.destroy()
    button2.destroy()


def homepage():
    print()

#top menu bar when user logins
def menus():
    # A MenuButton is a part of top-down menu which stays on the window all the time.
    # Every menubutton has its own functionality.
    topmenu = Menu(t)

    # file menu button
    filemenu = Menu(topmenu,tearoff=0)
    filemenu.add_command(label='New Email')
    # open template, read what info is needed, get info(messages,subject,files) and put in program
    filemenu.add_command(label='Open template')
    # store message/subject/name of files- into a txt file, file attachments will be in same directory as text file
    filemenu.add_command(label='Save Email as template')
    #opens a file widget and allows user to specify which txt file to use in program
    filemenu.add_command(label='Open Email list File (txt file)')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=t.quit)
    topmenu.add_cascade(label='File', menu=filemenu)
    
    
    # settings menu button
    settingsmenu = Menu(topmenu,tearoff=0)
    settingsmenu.add_command(label='Options')
    topmenu.add_cascade(label='Settings', menu=settingsmenu)
 

    # help menu button
    helpmenu = Menu(topmenu,tearoff=0)
    helpmenu.add_command(label='About / Github Page', command=opengithub)
    # point to github wiki page
    helpmenu.add_command(label='Tool Documentation')
    # point to github issues page
    helpmenu.add_command(label='Report Bugs/Glitches/Issues')
    topmenu.add_cascade(label='Help', menu=helpmenu)
    #applys the top menu bar to window
    t.config(menu=topmenu)


startup()

t.mainloop()
