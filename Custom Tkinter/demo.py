from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Custom Tkinter")
root.geometry("600x350")


l1 = customtkinter.CTkLabel(root,text="Key Q : ").grid(row=1,column=1,padx=20)
l1 = customtkinter.CTkLabel(root,text="Using Key Q you want to stop speaking AI half of the Path").grid(row=1,column=2)

l1 = customtkinter.CTkLabel(root,text="Key Q : ").grid(row=2,column=1,padx=20)
l1 = customtkinter.CTkLabel(root,text="Using Key Q you want to stop speaking AI half of the Path").grid(row=2,column=2)

l1 = customtkinter.CTkLabel(root,text="Key Q : ").grid(row=3,column=1,padx=20)
l1 = customtkinter.CTkLabel(root,text="Using Key Q you want to stop speaking AI half of the Path").grid(row=3,column=2)

l1 = customtkinter.CTkLabel(root,text="Key Q : ").grid(row=5,column=1,padx=20)
l1 = customtkinter.CTkLabel(root,text="Using Key Q you want to stop speaking AI half of the Path").grid(row=5,column=2)

l1 = customtkinter.CTkLabel(root,text="Key Q : ").grid(row=6,column=1,padx=20)
l1 = customtkinter.CTkLabel(root,text="Using Key Q you want to stop speaking AI half of the Path").grid(row=6,column=2)

l1 = customtkinter.CTkLabel(root,text="Key Q : ").grid(row=4,column=1,padx=20)
l1 = customtkinter.CTkLabel(root,text="Using Key Q you want to stop speaking AI half of the Path").grid(row=4,column=2)

root.mainloop()
