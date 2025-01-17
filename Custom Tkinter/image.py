from PIL import Image
from tkinter import *
import customtkinter
import PIL.Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Custom Tkinter")
root.geometry("600x350")

# image = Image("coder.jpg")

my_image = customtkinter.CTkImage(light_image=PIL.Image.open(
    "coder.png"), dark_image=PIL.Image.open("coder.png"), size=(50, 50))
image_label = customtkinter.CTkLabel(root, image=my_image, text="").pack()

button = customtkinter.CTkButton(
    root, image="coder.png").pack()


root.mainloop()
