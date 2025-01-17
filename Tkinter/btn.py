from tkinter import *

root = Tk()

root.geometry("400x400")
root.title("Basic GUI")


button1 = Button(root, text="Add", font=(
    "Arial", 15, "bold"), bg="red", fg="White", cursor="hand2", width=20, height=2)
button1.grid(row=1, column=1, padx=50, pady=50)


root.mainloop()
