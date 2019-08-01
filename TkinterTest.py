from tkinter import *
def doStuff():
    print("HI")
window=Tk()
window.geometry("400x400")
window.title("Welcome")
text1=Label(window,text="Test",font=("arial",20,"bold"))
text1.pack()

button1=Button(window,text="Press me",relief=RAISED,COMMAND=doStuff)
window.mainloop()
