from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")

#  Swich


def switch_event():
    print("switch toggled, current value:", switch_var.get())


switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(root, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off").pack()

root.mainloop()
