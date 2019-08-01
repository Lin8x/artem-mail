from tkinter import *
from tkinter import messagebox
import sys


def doStuff():
    print("HI")


def quit():
    sys.exit()


def prank():
    for i in range(1):
        messagebox.showinfo(
            "HEHEHEHEHEH", "HAHA your ugly")
        messagebox.showwarning("LOLOLOLOLOLOL", "you are gay")


window = Tk()
window.geometry("500x500")
window.title("Welcome")
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Email", command=doStuff)
filemenu.add_command(label="Save Email", command=doStuff)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Report Bug", command=doStuff)
helpmenu.add_command(label="Send Feedback", command=doStuff)
menubar.add_cascade(label="Help", menu=helpmenu)


text1 = Label(window, text="Testing window", font=("arial", 20, "bold"))
text1.pack()

button1 = Button(window, text="Press me", relief=RAISED,
                 command=doStuff, padx=20, pady=5, bd=4)
button2 = Button(window, text="Prank", relief=GROOVE,
                 command=prank, padx=20, pady=5, bd=4)
quitButton = Button(window, text="Quit", relief=RIDGE, command=quit, height=3, width=10, bd=4, font=(
    "arial", 10), activebackground="red", activeforeground="yellow")
button1.pack()

quitButton.pack()
button2.pack()
window.config(menu=menubar)
window.mainloop()
