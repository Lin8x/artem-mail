#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import sys
# from pillow import Image, ImageTk

t = Tk()  # where m is the name of the main window object

# theme Decal functions here {


def topDecalBar():
    # top bar here
    image = Image.open("topbar.jpg")
    image = image.resize((500, 20), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo  # keep a reference!
    label.pack()


def addHelpMenu(tkobject):
    '''returns a Menu object'''
    helpmenu = Menu(tkobject, tearoff=0)
    helpmenu.add_command(label='About / Github Page', command=opengithub)
    # point to github wiki page
    helpmenu.add_command(label='Tool Documentation',
                         command=lambda: opengithub(2))
    # point to github issues page
    helpmenu.add_command(label='Report Bugs/Glitches/Issues',
                         command=lambda: opengithub(1))
    return helpmenu


def setTopBarMenus():
    # A MenuButton is a part of top-down menu which stays on the window all the time.
    # Every menubutton has its own functionality.
    topmenu = Menu(t)

    # file menu button
    filemenu = Menu(topmenu, tearoff=0)
    filemenu.add_command(label='New Email')
    # open template, read what info is needed, get info(messages,subject,files) and put in program
    filemenu.add_command(label='Open template')
    # store message/subject/name of files- into a txt file, file attachments will be in same directory as text file
    filemenu.add_command(label='Save Email as template')
    # opens a file widget and allows user to specify which txt file to use in program
    filemenu.add_command(label='Open Email list File (txt file)')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=sys.exit)
    filemenu.add_command(label="Signout", command=loginpage)
    topmenu.add_cascade(label='File', menu=filemenu)

    # settings menu button
    settingsmenu = Menu(topmenu, tearoff=0)
    settingsmenu.add_command(label='Options')
    topmenu.add_cascade(label='Settings', menu=settingsmenu)

    # help menu button
    helpmenu = addHelpMenu(topmenu)
    topmenu.add_cascade(label='Help', menu=helpmenu)
    # applys the top menu bar to window
    t.config(menu=topmenu)

# } Decal functions
# login page stuff here {


def loginpage():
    menu = Menu(t)
    # help top menu bar for login screen
    helpmenu = addHelpMenu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    t.config(menu=menu)

    # logo here
    topDecalBar()
    image = Image.open("artemlogo.png")  # u need PNG file to store image Alpha
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
    # pasword shows up as * when typing
    E2 = Entry(t, bd=5, relief=GROOVE, show="*")
    # empty label as spacer between entry and buttons
    spacer = Label(text=" ")
    label1.pack()
    E1.pack()
    label2.pack()
    E2.pack()
    spacer.pack()

    # Button to quit the tool
    button2 = Button(t, text='Quit The Tool',
                     width=20, bd=3, command=sys.exit)
    button1 = Button(t, text='Enter', width=20, bd=3,
                     command=lambda: checkLogin(E1, E2))
    button1.pack()
    button2.pack()
    t.mainloop()


def checkLogin(userInput, passInput):
    if userInput.get() == "" or passInput.get() == "":
        messagebox.showerror(
            "Invalid Input", "you entered nothing\nPlease try again")
    elif len(userInput.get()) > 30 or len(userInput.get()) > 30:
        messagebox.showerror(
            "Invalid Input", "you have reached the max character threshold\nPlease try again")
    elif userInput.get().find("@") != -1:
        messagebox.showerror(
            "Detected @ symbol", "Please enter only the username \nwithout @gmail.com")
    else:
        for i in t.winfo_children():  # loops through all children(widgets)
            i.destroy()
        homepage()

# } login page stuff


def homepage():
    topDecalBar()
    setTopBarMenus()


def opengithub(site=0):  # dynamic github site opener
    # 0= home git page
    # 1= report issue site
    # 2= wiki page
    url = "https://github.com/Lin8x/artem-mail"
    if site == 1:
        url += "/issues"
    elif site == 2:
        url += "/wiki"

    # os.system("open https://github.com/Lin8x/artem-mail") # this only works for MAC
    # cross platform(new=2 opens a tab if webbroswer is already open)
    webbrowser.open(url, new=2, autoraise=True)


def startup():
    t.title("Artem Mail Tool")  # title of the tool
    t.geometry("500x400")  # Size of window
    TITLE_FONT = ("Helvetica", 18, "bold")  # The font of words

    # A frane is a rectangular region on the screen
    # frame = Frame(t)
    # frame.pack()
    bottomframe = Frame(t)
    bottomframe.pack(side=BOTTOM)

    # A Canvas is used to draw pictures and other complex layout like graphics, text and widgets.
    # c = Canvas(t, width=0, height=0)
    # c.pack()
    # canvas_height = 20
    # canvas_width = 200

    loginpage()


startup()
