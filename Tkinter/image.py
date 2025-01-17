from tkinter import *

root = Tk()

root.geometry('700x500')
root.title("Place Image")

# .png file is must for adding image


img1 = PhotoImage(file='img1.png')
lb = Label(root, image=img1).place(x=0, y=0)


root.mainloop()
