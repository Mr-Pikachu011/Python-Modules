
from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Basic GUI")


mainframe = Frame(root, bd=5, relief=GROOVE, bg="grey")

tl = Label(mainframe, text='Mr_Pikachu', font=(
    "Arial", 20, "bold"), bg="red", fg="white")
tl.place(x=25, y=5, width=300, height=30)

mainframe.place(x=0, y=0, width=350, height=350)


labalframe = LabelFrame(mainframe, text='Inside', font=(
    "Arial", 10, "bold"), bg="white", fg="red")
labalframe.place(x=10, y=45, width=150, height=100)

root.mainloop()
