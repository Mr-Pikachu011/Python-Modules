from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")


# OptionMenu
# without variable
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


optionmenu = customtkinter.CTkOptionMenu(root, values=["option 1", "option 2"],
                                         command=optionmenu_callback).pack()

# with Variable


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


optionmenu_var = customtkinter.StringVar(value="option 2")
optionmenu = customtkinter.CTkOptionMenu(root, values=["option 1", "option 2"],
                                         command=optionmenu_callback,
                                         variable=optionmenu_var).pack()

root.mainloop()
