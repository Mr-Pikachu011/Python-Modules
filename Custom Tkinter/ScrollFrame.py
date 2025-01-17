from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("Custom Tkinter")
root.geometry("600x350")


# scrollable_frame
scrollable_frame = customtkinter.CTkScrollableFrame(
    root, width=200, height=200).pack()


class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=1, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=2, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=3, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=4, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=5, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=6, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=7, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=8, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=9, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=10, column=0, padx=20)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=11, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(
            master=self, width=300, height=200, corner_radius=0, fg_color="transparent")
        self.my_frame.grid(row=0, column=0, sticky="nsew")


app = App()
app.mainloop()

root.mainloop()
