from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")


# customtkinter.CTkButton(root, text="Hello World!").pack()

button = customtkinter.CTkButton(
    root, fg_color="red") .pack()  # single color name
button = customtkinter.CTkButton(
    root, fg_color="#FF0000").pack()  # single hex string
button = customtkinter.CTkButton(
    root, fg_color=("#DB3E39", "#821D1A")) .pack()  # tuple color
root.mainloop()
