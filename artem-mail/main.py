#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk,Image
import os

t = Tk() # where m is the name of the main window object

def topbar():
    #top bar here
    image = Image.open("topbar.jpg")
    image = image.resize((500, 20), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.pack()

def opengithub():
    
    os.system("open https://github.com/Lin8x/artem-mail")

def startup():
    
    t.title("Artem Mail Tool") # title of the tool
    t.geometry("500x400") # Size of window
    TITLE_FONT = ("Helvetica", 18, "bold") # The font of words

    #A frane is a rectangular region on the screen
    frame = Frame(t) 
    frame.pack()
    bottomframe = Frame(t)
    bottomframe.pack( side = BOTTOM )

    #A Canvas is used to draw pictures and other complex layout like graphics, text and widgets.
    c = Canvas(t, width=0, height=0) 
    c.pack() 
    canvas_height=20
    canvas_width=200

    loginpage()

def loginpage():
    
    menu = Menu(t) 
    t.config(menu=menu)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About / Github Page', command=opengithub)
    helpmenu.add_command(label='Tool Documentation')
    helpmenu.add_command(label='Report Bugs/Glitches/Issues')

    topbar()

    #logo here
    image = Image.open("artemlogo.JPG")
    image = image.resize((200, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.pack()
    
    #Everything below here is the buttons

    #Entry/Text Input
    label1 = Label(t, text="Gmail Username")
    E1 = Entry(t, bd =5)

    label2 = Label(t, text="Gmail Password")
    E2 = Entry(t, bd =5)

    label1.pack()
    E1.pack()
    label2.pack()
    E2.pack()

    #Button to quit the tool
    button2 = Button(t, text='Quit The Tool', width=20, command=t.destroy)
    button1 = Button(t, text='Enter', width=20, command= lambda: logindestroy(label, label1, label2, E1, E2, button1, button2)) 
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
    

def menus():
    #A MenuButton is a part of top-down menu which stays on the window all the time.
    #Every menubutton has its own functionality.
    menu = Menu(t) 
    t.config(menu=menu)

    #file menu button
    filemenu = Menu(menu) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='New Email') 
    filemenu.add_command(label='Open Email File (txt file)') 
    filemenu.add_separator() 
    filemenu.add_command(label='Exit', command=t.quit)

    #settings menu button
    settingsmenu = Menu(menu)
    menu.add_cascade(label='Settings', menu=settingsmenu)
    settingsmenu.add_command(label='Options')

    #help menu button
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About / Github Page', command=opengithub)
    helpmenu.add_command(label='Tool Documentation')
    helpmenu.add_command(label='Report Bugs/Glitches/Issues')

startup()

t.mainloop() 

