from tkinter import *


def msg():
    print("Welcome")


win = Tk()
win.title("CCIT")
win.geometry("500x400")
btn = Button(win, text="Show", command=msg)
btn.pack()
win.mainloop()
