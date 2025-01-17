from tkinter import *
from tkinter.ttk import Combobox
root = Tk()
root.geometry("400x400")
root.title("Basic GUI")

# functioning of combobox
cat = ["Select", "Cloth", "Frute", "Book"]
cloth1 = ["Shirt", "tesart", "pant"]

cb = Combobox(root, value=cat, font=(
    "Arial", 10, "bold"), width=20, state="readonly")
cb.current(0)
cb.grid(row=1, column=1, sticky=W, padx=10, pady=10)

cb1 = Combobox(root, value=cloth1, font=(
    "Arial", 10, "bold"), width=20, state="readonly")
cb1.current(0)
cb1.grid(row=2, column=1, sticky=W, padx=10, pady=10)


root.mainloop()
