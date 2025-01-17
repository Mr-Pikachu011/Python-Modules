from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Custom Tkinter")
root.geometry("600x350")


def button_event():
    print("button pressed")


button = customtkinter.CTkButton(
    root, text="CTkButton", command=button_event).pack()


root.mainloop()
