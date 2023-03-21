from tkinter import *


def ok():
    print("You Clicked OK")


def cancel():
    print("You Clicked Cancel")


win = Tk()
win.config(bg="purple")
win.title("OK or Cancel")
win.geometry("500x300")
btn1 = Button(win, text="OK", command=ok)
btn2 = Button(win, text="Cancel", command=cancel)
btn1.pack()
btn2.pack()
win.mainloop()
