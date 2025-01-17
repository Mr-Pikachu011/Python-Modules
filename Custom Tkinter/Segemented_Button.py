from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")


# Segmrnt button
# without variable
def segmented_button_callback(value):
    print("segmented button clicked:", value)


segemented_button = customtkinter.CTkSegmentedButton(root, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback).pack()
# segemented_button.set("Value 1")

# with Variable


def segmented_button_callback(value):
    print("segmented button clicked:", value)


segemented_button_var = customtkinter.StringVar(value="Value 1")
segemented_button = customtkinter.CTkSegmentedButton(root, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback,
                                                     variable=segemented_button_var).pack()

root.mainloop()
