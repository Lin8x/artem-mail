#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import webbrowser
import sys
import os
from cryptography.fernet import Fernet
import emailsender

t = Tk()  # where m is the name of the main window object
Recipient_fileUploadName = StringVar()
Files_fileUploadName = []

recipient_Data = ""  # reference entry / file data


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
    helpmenu.add_command(label='About Artem', command=lambda: openSite(3))
    helpmenu.add_command(label='Github Page', command=openSite)
    # point to github wiki page
    helpmenu.add_command(label='Tool Documentation',
                         command=lambda: openSite(2))
    # point to github issues page
    helpmenu.add_command(label='Report Bugs/Glitches/Issues',
                         command=lambda: openSite(1))
    return helpmenu


# this brings in artem logo image
def addlogo():
    # logo here
    topDecalBar()
    image = Image.open("artemlogo.png")  # u need PNG file to store image Alpha
    image = image.resize((200, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo  # keep a reference!
    label.pack()


def setTopBarMenus():
    # A MenuButton is a part of top-down menu which stays on the window all the time.
    # Every menubutton has its own functionality.
    topmenu = Menu(t)

    # file menu button
    filemenu = Menu(topmenu, tearoff=0)
    filemenu.add_command(label='New Email', command=restartHome)
    # open template, read what info is needed, get info(messages,subject,files) and put in program
    filemenu.add_command(label='Open Template')
    # store message/subject/name of files- into a txt file, file attachments will be in same directory as text file
    filemenu.add_command(label='Save Email as Template')
    # opens a file widget and allows user to specify which txt file to use in program
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
    t.geometry("500x450")  # Size of window
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
    mainFont = ("arial", 11)
    # Entry/Text Input
    label1 = Label(t, text="Email Username", font=mainFont)
    E1 = Entry(t, bd=3, relief=GROOVE, width=30, font=mainFont)

    label2 = Label(t, text="Email Password", font=mainFont)
    # pasword shows up as * when typing
    E2 = Entry(t, bd=3, relief=GROOVE, width=30, show="*", font=mainFont)
    # empty label as spacer between entry and buttons
    spacer = Label(text=" ")
    label1.pack()
    E1.pack()
    label2.pack()
    E2.pack()
    # remember me checkboc
    remember = IntVar()
    rememberCheck = Checkbutton(t, text="  Remeber me", variable=remember, font=mainFont)  # 0=off 1=on
    rememberCheck.pack()
    spacer.pack()

    quitButton = Button(t, text='Quit The Tool', width=20, height=2, relief=GROOVE, bd=3, font=("arial", 10, "bold"),
                        command=sys.exit)
    loginButton = Button(t, text='Login in', width=20, height=2, relief=GROOVE, bd=3, font=("arial", 10, "bold"),
                         command=lambda: checkLogin(E1, E2, remember.get(), loginButton))
    spacer2 = Label(t, text=" ")
    loginButton.pack()
    spacer2.pack()
    quitButton.pack()
    bottomDecalBar()
    # check if rememberMe file is there
    if os.path.exists("rememberMe.artem"):
        print("Found rememberMe.artem")
        with open("rememberMe.artem", "rb") as file:
            # marks the rememberMe checkbox
            # rememberCheck.select()
            data = file.read()
            file.close()
            # converts byte backinto a string for split()
            data = data.decode("utf-8")
            data = data.split("ZGFuaXNnYXk=")
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
        E1.config(bg="white")
        E2.config(bg="white")
        print("Cant find rememberMe file")

    t.mainloop()


def checkLogin(userInput, passInput, storeUserandPass, button):  # prevents invalid inputs
    button.config(text="Loading...")
    if userInput.get() == "" or passInput.get() == "":
        messagebox.showerror(
            "Invalid Input", "You entered nothing\nPlease try again")
    elif len(userInput.get()) > 30 or len(userInput.get()) > 30:
        messagebox.showerror(
            "Invalid Input", "You have reached the max character threshold\nPlease try again")
    else:
        can_pass = emailsender.login_to_email(userInput.get(), passInput.get())
        # print("Variavle :"+str(storeUserandPass))
        if storeUserandPass == 1:
            # stores new info into system
            key = Fernet.generate_key()
            fernet = Fernet(key)
            info = userInput.get() + " " + passInput.get()
            encryptedData = fernet.encrypt(info.encode("utf-8"))
            with open("rememberMe.artem", 'wb') as f:
                f.write(key)
                f.write("ZGFuaXNnYXk=".encode("utf-8"))
                f.write(encryptedData)
                f.close()
                print("Created encrpted file name: rememberMe.artem")

            # with open("rememberMe.artem", "wb") as file:
            #     info=userInput.get()+" "+passInput.get()
            #     file.write(info.encode('utf-8'))# converts to byte
            #     print("Saved file as rememberMe.artem")
            #     file.close()
            # with open("rememberMe.artem","rb") as read:
            #     info=read.read()
            #     print(info.decode('utf-8'))#converts back to string
        if can_pass:
            homepage()
        else:
            button.config(text="Login in")
            messagebox.showerror(
                "Incorrect Username or Password.",
                "If your username and password is correct but you are still getting this error\n Visit the troubleshooting page https://github.com/asian-code/artem-mail/wiki")


# } login page stuff

# Main page stuff here {
def selectRecipentFile():
    global recipient_Data
    t.filename = filedialog.askopenfilename(
        initialdir="~/", title="Select txt file...", filetypes=(("Text Files", "*.txt"), ("all files", "*.*")))
    global Recipient_fileUploadName
    Recipient_fileUploadName.set(t.filename)

    recipient_Data = t.filename  # to reference later
    # Recipient_fileUploadName = t.filename
    print(Recipient_fileUploadName)


def get_file_attachment():
    t.filename = filedialog.askopenfilename(
        initialdir="~/", title="Select File", filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
    Files_fileUploadName.append(t.filename)
    print(Files_fileUploadName)


def helpMessage():
    messagebox.showinfo("Help",
                        "Format- (Name);(Email)\n(Name) is optional\n\nExample:\nJohn Smith;johnny@gmail.com\n;hellokitty@gmail.com\nAlex Gomez;trollmaster@yahoo.com")


def sentTo_Menu(section, makeMeGone, option=0):
    makeMeGone.destroy()
    if option == 0:  # upload txt file
        selectrecipentButton = Button(section, text="Upload file", relief=GROOVE, font=("arial", 10),
                                      command=selectRecipentFile, bd=3)
        text = Label(section, text="Upload a txt file :", font=("arial", 10))
        # var = selectrecipentButton.get
        fileLoc = Label(section, textvariable=Recipient_fileUploadName)  # os.path.basename(Recipient_fileUploadName)
        text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        selectrecipentButton.grid(row=0, column=3, padx=10, pady=10)
        fileLoc.grid(row=0, column=5, padx=10, pady=10)
    else:  # enter all recipents
        BIGemails = Text(section, height=5, width=80, font=("arial", 10))
        scrll = Scrollbar(section, command=BIGemails.yview)
        BIGemails.config(yscrollcommand=scrll.set)
        BIGemails.insert("1.0",
                         "# Example:\nJohn Smith;johnny@gmail.com\nJames William;willi@gmail.com\n;kittylover@gmail.com")
        BIGemails.grid(row=0, pady=15, padx=10)
        scrll.grid(row=0, column=81, sticky="NS")
        questionButton = Button(section, text="?", font=("arial", 15, "bold"), relief=GROOVE, bd=3, width=2,
                                command=helpMessage)
        questionButton.grid(row=0, column=100, padx=3, pady=1)


def restartHome():
    global Recipient_fileUploadName, Files_fileUploadName
    Recipient_fileUploadName = StringVar()
    Files_fileUploadName = []
    homepage()


def sendMessage(recipientStuff, sub, mess, files=[]):
    sendto = ""
    # get recipients

    if recipient_Data == "" or len(recipient_Data) < 2:
        # entry

        print(recipient_Data)
        # sendto = Recipient_fileUploadName
    else:  # from file

        with open(str(Recipient_fileUploadName), "r")as f:
            data = f.readlines()
            print(data)
            # sendto = data[0]
            f.close()

    # checks if recipient file/entry is emtpy(prevents sending nobody)
    # checks if subject and message is empty (prevents sending empty messages)
    # show a (red *) next to boxes that need to have a message? or show a pop up message?
    # emailsender.sendEmail(sendto, sub, mess)


def onFrameConfigure(canvas):  # megaScrollbar on the right side of screen
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


def homepage():
    t.geometry("700x730")
    clearScreen()
    setTopBarMenus()
    # title = Label(t, text="Mail (Under development)", font=("arial", 12, "bold"))

    canvas = Canvas(t, bd=0, highlightthickness=0, relief='ridge')  # background="#ffffff"
    megaScrollbar = Scrollbar(t, command=canvas.yview, width=25)
    window = Frame(canvas, bd=0, highlightthickness=0)  # background="#ffffff"
    canvas.configure(yscrollcommand=megaScrollbar.set)

    section1 = LabelFrame(window, text="1.Send To")
    section2 = LabelFrame(window, text="2.Subject")
    section3 = LabelFrame(window, text="3.Message")
    section4 = LabelFrame(window, text="4.Files")
    subjectInput = Entry(section2, bd=1, width=93)

    # menu button for sent to section
    sendMenu = Menubutton(section1, text="Select Option")
    sendMenu.menu = Menu(sendMenu, tearoff=0)
    sendMenu["menu"] = sendMenu.menu
    sendMenu.menu.add_command(label="1. Emails in file", command=lambda: sentTo_Menu(section1, sendMenu))
    sendMenu.menu.add_command(label="2. Enter recipients", command=lambda: sentTo_Menu(section1, sendMenu, option=1))

    messageTextBox = Text(section3, bd=1, width=60, height=15)
    messageScroll = Scrollbar(section3, command=messageTextBox.yview, orient=VERTICAL, width=25)
    messageTextBox.config(yscrollcommand=messageScroll.set)
    AddAttachments = Button(section4, text="Add Attachments", relief=GROOVE, command=get_file_attachment)

    # Layout is designed here
    megaScrollbar.pack(side=RIGHT, fill=Y)
    addlogo()
    canvas.pack(fill=BOTH, expand=True)
    canvas.create_window((4, 4), window=window, anchor="nw")
    window.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    # Send to -section
    section1.pack(fill=X)
    sendMenu.config(relief=RAISED)
    sendMenu.grid(row=0, column=0, padx=10, pady=10)
    # Subject-section
    section2.pack(fill=X)
    subjectInput.grid(sticky="WE", padx=10, pady=10)
    # Message-section
    section3.pack(fill=X)
    messageTextBox.grid(row=0, padx=10, pady=10, sticky="W")
    messageScroll.grid(row=0, column=100, sticky="NS", rowspan=5, columnspan=3)
    # files-section
    section4.pack(fill=X)
    AddAttachments.grid(row=0, column=0, pady=10, padx=10)
    # End buttons
    buttonContainer = Frame(window)
    buttonContainer.pack()
    sendButton = Button(buttonContainer, text="Send Email", font=("arial", 10, "bold"), bd=3, relief=RAISED,
                        width=30, height=2, fg="green",
                        command=lambda: sendMessage(subjectInput.get(), messageTextBox.get("1.0", END),
                                                    Files_fileUploadName))
    restartButton = Button(buttonContainer, text="Restart", font=("arial", 10, "bold"), bd=3, relief=RAISED,
                           command=restartHome, width=30, height=2, fg="red")

    # image1 = Image.open("RestartButton.png")
    # image1 = image1.resize((100, 100), Image.ANTIALIAS)
    # RestartImage = ImageTk.PhotoImage(image1)
    # image2 = Image.open("SendButton.png")
    # SendImage = SendImage.resize((100, 100), Image.ANTIALIAS)
    # SendImage = ImageTk.PhotoImage(image2)
    # WTF DAN HELP ME!!!!!!!!!!!! IMAGES FOR MY BUTTONS DONT WORK ***************************************************
    # sendButton = Button(buttonContainer, image=SendImage, height=40, width=200)
    # restartButton = Button(buttonContainer, image=RestartImage, height=40, width=200, command=restartHome)

    restartButton.grid(row=0, sticky=W, padx=10, pady=10)
    sendButton.grid(row=0, column=1, sticky=E, padx=10, pady=10)
    bottomDecalBar()  # this stay at bottom

    # } main page


def openSite(site=0):  # dynamic github site opener
    # 0= home git page
    # 1= report issue site
    # 2= wiki page
    # 3=about Artem site
    url = "https://github.com/Lin8x/artem-mail"
    if site == 1:
        url += "/issues"
    elif site == 2:
        url += "/wiki"
    elif site == 3:
        url = "https://www.artemleaders.com/about.html"

    # os.system("open https://github.com/Lin8x/artem-mail") # this only works for MAC
    # cross platform(new=2 opens a tab if webbroswer is already open)
    webbrowser.open(url, new=2, autoraise=True)


def startup():
    t.title("Artem Mail Tool")  # title of the tool
    TITLE_FONT = ("Helvetica", 18, "bold")  # The font of words

    # A frane is a rectangular region on the screen
    # frame = Frame(t)
    # frame.pack()
    # bottomframe = Frame(t)
    # bottomframe.pack(side=BOTTOM)

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
