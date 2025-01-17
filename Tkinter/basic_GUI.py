# build GUI (Grafical Uaser Interface) using Python

# In python we can create GUI Using Tkinter

from tkinter import *

root = Tk()

root.geometry("100x100")
root.title("Basic GUI")


mylable = Label(root, text="Hello World").pack()


root.mainloop()
