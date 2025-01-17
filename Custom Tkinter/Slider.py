from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")


# slider
def slider_event(value):
    print(value)


slider = customtkinter.CTkSlider(
    root, from_=0, to=100, command=slider_event).pack()


root.mainloop()
