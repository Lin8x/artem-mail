#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import webbrowser
import sys
import os
from cryptography.fernet import Fernet
# from pillow import Image, ImageTk

t = Tk()  # where m is the name of the main window object

# theme Decal functions here {


def topDecalBar():
    # top bar here
    image = Image.open("topbar.jpg")
    image = image.resize((image.size[0], 20), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo  # keep a reference!
    label.pack(fill=X)


def bottomDecalBar():
    image = Image.open("topbar.jpg")
    image = image.resize((image.size[0], 20), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo  # keep a reference!
    label.pack(side=BOTTOM, fill=X)


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
    filemenu.add_command(label="Signout", command=loginpage)
    filemenu.add_command(label='Exit', command=sys.exit)
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
    clearScreen()
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
    # remember me checkboc
    remember = IntVar()
    rememberCheck = Checkbutton(
        t, text="  Remeber me", variable=remember, font=("arial", 10))  # 0=off 1=on
    rememberCheck.pack()
    spacer.pack()

    # Button to quit the tool
    button2 = Button(t, text='Quit The Tool',
                     width=20, bd=3, command=sys.exit)
    button1 = Button(t, text='Login in', width=20, bd=3,
                     command=lambda: checkLogin(E1, E2, remember.get()))

    button1.pack()
    button2.pack()
    bottomDecalBar()
    # check if rememberMe file is there
    if os.path.exists("rememberMe.artem"):
        print("Found rememberMe.artem")
        with open("rememberMe.artem", "rb") as file:
            # marks the rememberMe checkbox
            rememberCheck.select()
            data = file.read()
            file.close()
            # converts byte backinto a string for split()
            data = data.decode("utf-8")
            data = data.split("danisgay")
            key = data[0].encode("utf-8")  # gets the key stored in file
            fernet = Fernet(key)
            encrypted = fernet.decrypt(data[1].encode("utf-8"))
            # print("Encrypted data:"+encrypted.decode("utf-8"))
            encrypted = encrypted.split()
            E1.insert(0, encrypted[0])
            E2.insert(0, encrypted[1])
            E1.config(bg="#f8f983")
            E2.config(bg="#f8f983")
    else:
        # unmarks the checkbox
        rememberCheck.deselect()
        print("Cant find rememberMe file")

    t.mainloop()


def checkLogin(userInput, passInput, storeUserandPass):  # prevents invalid inputs
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
        # print("Variavle :"+str(storeUserandPass))
        if storeUserandPass == 1:
            # stores new info into system
            key = Fernet.generate_key()
            fernet = Fernet(key)
            info = userInput.get()+" "+passInput.get()
            encryptedData = fernet.encrypt(info.encode("utf-8"))
            with open("rememberMe.artem", 'wb') as f:
                f.write(key)
                f.write("danisgay".encode("utf-8"))
                f.write(encryptedData)
                f.close()
                print("Created encrpted file name: remeberMe.artem")

            # with open("rememberMe.artem", "wb") as file:
            #     info=userInput.get()+" "+passInput.get()
            #     file.write(info.encode('utf-8'))# converts to byte
            #     print("Saved file as rememberMe.artem")
            #     file.close()
            # with open("rememberMe.artem","rb") as read:
            #     info=read.read()
            #     print(info.decode('utf-8'))#converts back to string
        clearScreen()
        homepage()

# } login page stuff


def selectRecipentFile():

    t.filename = filedialog.askopenfilename(
        initialdir="~/Downloads", title="Select txt file...", filetypes=(("Text Files", "*.txt"), ("all files", "*.*")))
    return t.filename
def get_file_attachment():
    t.filename = filedialog.askopenfilename(
        initialdir="~/Downloads", title="Select File", filetypes=(("PDF files","*.pdf"),("all files", "*.*")))
    return t.filename


def homepage():
    t.geometry("700x600")
    topDecalBar()
    setTopBarMenus()
    # homepage widgets go here
    title = Label(t, text="Mail (Under development)",
                  font=("arial", 12, "bold"))
    section1 = LabelFrame(t, text="Send To")
    send1text = Label(
        section1, text="1) Emails in file:", font=("arial", 10))
    send2text = Label(
        section1, text="2) Artem Subscribers\n\tPassword   :", font=("arial", 10))
    selectrecipentButton = Button(section1, text="Upload file", relief=GROOVE, font=(
        "arial", 10), command=selectRecipentFile, bd=3)
    recipent = Entry(section1, bd=5, relief=GROOVE)
    section2 = LabelFrame(t, text="Subject")
    section3 = LabelFrame(t, text="Files")
    subjectInput = Entry(section2, relief=GROOVE, bd=5)
    fileAttachments=Button(section3,text="Upload file",font=("arial", 10))
    selectFileButton = Button(section1, text="Upload file", relief=GROOVE, font=(
        "arial", 10), command=get_file_attachment, bd=3)
    title.pack(side=TOP)
    section1.pack(fill=X,)
    send1text.grid(row=0, column=0)
    selectFileButton.grid(row=0, column=1)
    send2text.grid(row=1,column=0)
    recipent.grid(row=1, column=1)
    section2.pack(fill=X)
    subjectInput.pack()
    section3.pack(fill=X)
    fileAttachments.pack()

    bottomDecalBar()  # this stay at bottom


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


def clearScreen():
    for i in t.winfo_children():  # loops through all children(widgets)
        i.destroy()


startup()
