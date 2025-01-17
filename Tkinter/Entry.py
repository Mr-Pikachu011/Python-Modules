from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Basic GUI")

tl = Entry(root, font=("Arial", 20, "bold"), width=20)
tl.grid(row=1, column=1, sticky=W)


root.mainloop()
