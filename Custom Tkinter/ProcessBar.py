from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")


# progreass bar
progressbar = customtkinter.CTkProgressBar(
    root, orientation="horizontal").pack()

root.mainloop()
