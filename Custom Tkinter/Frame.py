from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")


# frame
frame = customtkinter.CTkFrame(master=root, width=600, height=350).place(x=0,y=0)

root.mainloop()
