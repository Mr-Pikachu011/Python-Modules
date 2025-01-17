from tkinter import *

root = Tk()

root.geometry("400x400")
root.title("Basic GUI")


billarea = LabelFrame(root, text="BIll Area", font=(
    "Arial", 10, "bold"), bg="white", fg="red", padx=20, pady=20)
billarea.place(x=0, y=0, width=360, height=100)

scroll_y = Scrollbar(billarea, orient=VERTICAL)
textarea = Text(billarea, yscrollcommand=scroll_y.set, font=(
    "Arial", 10, "bold"), bg="white", fg="yellow",)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=1)

# billarea = LabelFrame(root, text="BIll Area", font=(
#     "Arial", 15, "bold"), bg="white", fg="red", width=550, height=200)
# billarea.grid(row=0, column=4, rowspan=6, padx=20, pady=18)

# scroll_y = Scrollbar(billarea, orient=VERTICAL)
# textarea = Text(billarea, yscrollcommand=scroll_y.set, font=(
#     "Arial", 10, "bold"), bg="white", fg="yellow",)
# scroll_y.pack(side=RIGHT, fill=Y)
# scroll_y.config(command=textarea.yview)
# textarea.pack(fill=BOTH, expand=1)


root.mainloop()
