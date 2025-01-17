from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")


# combobox
# # with variable
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)


mesure = ["Select", "one   ", "two   ", "three ", "four  ",
          "five  ", "six   ", "seven ", "eight ", "nine   ", "ten   "]

combobox_var = customtkinter.StringVar(value=mesure)
combobox = customtkinter.CTkComboBox(root, values=mesure,
                                     command=combobox_callback, variable=combobox_var).pack()
combobox_var.set("option 2")

# without variable


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)


combobox = customtkinter.CTkComboBox(root, values=["option 1", "option 2"],
                                     command=combobox_callback).pack()


root.mainloop()
