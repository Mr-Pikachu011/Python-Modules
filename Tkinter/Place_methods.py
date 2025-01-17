from tkinter import *

root = Tk()

root.geometry("300x300")
root.title("Basic GUI")

# Different method to place the components

pack = Frame(root)
mylable = Label(pack, text="Hello World pack").pack()
pack.grid(row=1, column=1)


place = Frame(root)
mylable = Label(place, text="Hello World place").place(x=100, y=100)
place.grid(row=2, column=1)


grid = Frame(root)
mylable = Label(grid, text="Hello World grid").grid(row=1, column=1)
grid.grid(row=3, column=1)


root.mainloop()
