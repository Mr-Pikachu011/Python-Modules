from tkinter import *
from tkinter import ttk
import mysql.connector
# create table information (Name varchar(255),age int(3),mobile int(10),blood_group varchar(20)
# ,admid varchar(20),releas varchar(20), address varchar(255),payment int(20))
# create table information (Name,age,mobile,blood_group,admid,releas,address,payment)
def add_data():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="management" )
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO information (Name,age,mobile,blood_group,admid,releas,address,payment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    val = (name_entry.get(), age_entry.get(),Mobile_no_Entry.get(),blood_group_entry.get(),admit_date_entry.get(),release_date_entry.get(),address_entry.get(),payment_entry.get())
    mycursor.execute(sql, val)
    textarea.delete(1.0, END)
    textarea.insert(END,"\n \t\t\t Hospital Management System")
    textarea.insert(END,f"\n Name \t\t: {name_entry.get()}")
    textarea.insert(END,f"\n Age  \t\t: {age_entry.get()}")
    textarea.insert(END,f"\n Mobile no \t\t : {Mobile_no_Entry.get()}")
    textarea.insert(END,f"\n Blood Group \t  : {blood_group_entry.get()}")
    textarea.insert(END,f"\n Admit Date  \t  : {admit_date_entry.get()}")
    textarea.insert(END,f"\n Release Date : {release_date_entry.get()}")
    textarea.insert(END,f"\n Address      : {address_entry.get()}")
    textarea.insert(END,f"\n Payment     : {payment_entry.get()}")
    
    mydb.commit()
    

def show_data():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="management" )
    
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM information")

    myresult = mycursor.fetchall()
    textarea1.delete(1.0, END)
    textarea1.insert(END,"\n \t\t\t Hospital Management System")
    textarea1.insert(END,f"\n Name \t  Age  \t  MObile no  \t  Blood Group  \t  admit Date  \t  Release Date  \t  Address  \t   Payment")
        
    for x in myresult:
        textarea1.insert(END,f"\n {x[0]} \t  {x[1]}  \t  {x[2]}  \t  {x[3]}  \t  {x[4]}  \t  {x[5]}  \t  {x[6]}  \t   {x[7]}")

def delete1():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="management" )
    
    mycursor = mydb.cursor()
    sql = f"DELETE FROM information WHERE mobile = {str(mobile_no_entry1.get())}"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def delete():
    
    root1 = Tk()
    root1.geometry("210x120")
    root1.title("Basic GUI")
    
    global mobile_no_entry1
    mobile_no_entry1 = Entry(root1, font=("Arial", 12, ""), width=20)
    mobile_no_entry1.grid(row=0, column=1, sticky=W,pady=10,padx=10)
    mobile_no_entry1.insert(0, 'Mobile Number')
    
    delete1_button = Button(root1, text="Delete", font=(
    "Arial", 10, "bold"), bg="red", fg="White",width=22,height=2,command=delete1)
    delete1_button.grid(row=1, column=1,pady=10,padx=10)
    
    root1.mainloop()
    
    


root = Tk()
root.geometry("1100x700")
root.title("Basic GUI")


titleframe = Frame(root, bd=5, relief=GROOVE, bg="grey")

tl = Label(titleframe, text='Hospital Managemen System', font=(
    "Arial", 20, "bold"), fg="red", bg="grey")
tl.place(x=400, y=0)

titleframe.place(x=0, y=0, width=1100, height=50)


mainframe = Frame(root, bd=5, relief=GROOVE, bg="grey")
mainframe.place(x=0, y=50, width=1100, height=400)

labalframe = LabelFrame(mainframe, text='Patient Information', font=(
    "Arial", 10, "bold"), bg="grey", fg="red")
labalframe.place(x=10, y=0, width=500, height=380)

tl = Label(labalframe, text='Name of Pasent : ', font=(
    "Arial", 10, "bold"), bg="grey", fg="black").grid(row=0,column=0,sticky=W)
tl = Label(labalframe, text='Age : ', font=(
    "Arial", 10, "bold"), bg="grey", fg="black").grid(row=1,column=0,sticky=W)
tl = Label(labalframe, text='Mobile Number : ', font=(
    "Arial", 10, "bold"), bg="grey", fg="black").grid(row=2,column=0,sticky=W)
tl = Label(labalframe, text='Blood group : ', font=(
    "Arial", 10, "bold"), bg="grey", fg="black").grid(row=3,column=0,sticky=W)
tl = Label(labalframe, text='Admit Date : ', font=(
    "Arial", 10, "bold"), bg="grey", fg="black").grid(row=4,column=0,sticky=W)
tl = Label(labalframe, text='Realese Date : ', font=(
    "Arial", 10, "bold"), bg="grey", fg="black").grid(row=5,column=0,sticky=W)
tl = Label(labalframe, text='Permanent Address : ', font=(
    "Arial", 10, "bold"), bg="grey", fg="black").grid(row=6,column=0,sticky=W)
tl = Label(labalframe, text='Total Fee : ', font=(
    "Arial", 10, "bold"), bg="grey", fg="black").grid(row=7,column=0,sticky=W)


name_entry = Entry(labalframe, font=("Arial", 12, ""), width=20)
name_entry.grid(row=0, column=1, sticky=W,pady=10)
# name_entry.insert(0, 'Name')
age_entry = Entry(labalframe, font=("Arial", 12, ""), width=20)
age_entry.grid(row=1, column=1, sticky=W,pady=10)
# age_entry.insert(0, 0)
Mobile_no_Entry = Entry(labalframe, font=("Arial", 12, ""), width=20)
Mobile_no_Entry.grid(row=2, column=1, sticky=W,pady=10)
# Mobile_no_Entry.insert(0, 1111111111)
blood_group_entry = Entry(labalframe, font=("Arial", 12, ""), width=20)
blood_group_entry.grid(row=3, column=1, sticky=W,pady=10)
# blood_group_entry.insert(0, ' O+')
admit_date_entry = Entry(labalframe, font=("Arial", 12, ""), width=20)
admit_date_entry.grid(row=4, column=1, sticky=W,pady=10)
# admit_date_entry.insert(0, '1-1-2000')
release_date_entry = Entry(labalframe, font=("Arial", 12, ""), width=20)
release_date_entry.grid(row=5, column=1, sticky=W,pady=10)
# release_date_entry.insert(0, '1-1-2000')
address_entry = Entry(labalframe, font=("Arial", 12, ""), width=20)
address_entry.grid(row=6, column=1, sticky=W,pady=10)
# address_entry.insert(0, 'At. xyz')
payment_entry = Entry(labalframe, font=("Arial", 12, ""), width=20)
payment_entry.grid(row=7, column=1, sticky=W,pady=10)
# payment_entry.insert(0, 'Rs')



# Prescription

areaframe = LabelFrame(mainframe, text='Prescription', font=(
    "Arial", 10, "bold"), bg="grey", fg="red")
areaframe.place(x=515, y=0, width=570, height=380)

scroll_y = Scrollbar(areaframe, orient=VERTICAL)
textarea = Text(areaframe, yscrollcommand=scroll_y.set, font=(
    "Arial", 10, "bold"), bg="white", fg="black",)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=1)


# Buttons

buttonframe = Frame(root, bd=5, relief=GROOVE, bg="grey")
buttonframe.place(x=0, y=450, width=1100, height=60)

addpasent_button = Button(buttonframe, text="Add Pasent", font=(
    "Arial", 10, "bold"), bg="red", fg="White",width=33,height=2,command=add_data)
addpasent_button.grid(row=0, column=0)
pasentdata_button = Button(buttonframe, text="Pasent data", font=(
    "Arial", 10, "bold"), bg="red", fg="White",width=33,height=2,command=show_data)
pasentdata_button.grid(row=0, column=1)
delete_button = Button(buttonframe, text="Delete", font=(
    "Arial", 10, "bold"), bg="red", fg="White",width=33,height=2,command=delete)
delete_button.grid(row=0, column=3)
exit_button = Button(buttonframe, text="Exit", font=(
    "Arial", 10, "bold"), bg="red", fg="White",width=32,height=2,command=root.destroy)
exit_button.grid(row=0, column=4)



# data Frame

dataframe = Frame(root, bd=5, relief=GROOVE, bg="grey")
dataframe.place(x=0, y=510, width=1100, height=190)

scroll_y = Scrollbar(dataframe, orient=VERTICAL)
textarea1 = Text(dataframe, yscrollcommand=scroll_y.set, font=(
    "Arial", 10, "bold"), bg="white", fg="black",)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea1.pack(fill=BOTH, expand=1)


root.mainloop()