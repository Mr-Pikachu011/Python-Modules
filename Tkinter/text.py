from tkinter import *
root = Tk()
root.geometry("300x300")
root.title("Basic GUI")


tl = Label(root, text='Mr_Pikachu', font=(
    "Arial", 20, "bold"), bg="red", fg="white")
tl.place(x=0, y=0, width=300, height=30)


root.mainloop()
