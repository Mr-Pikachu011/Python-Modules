from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")


# CheckBox
def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())


check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(root, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off").pack()


root.mainloop()
