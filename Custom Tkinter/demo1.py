from tkinter import *
from tkinter.ttk import Combobox
import mysql.connector
import random
from tkinter import messagebox


def main(text1, row1, column1,):
    labal = Label(mainframe, text=text1, font=(
        "Arial", 15, "bold"), bg="grey", fg="black")
    labal.grid(row=row1, column=column1, padx=15, pady=5, sticky=W)


def total1(text1, row1, column1,):
    labal = Label(total_frame, text=text1, font=(
        "Arial", 15, ""), bg="grey", fg="black")
    labal.grid(row=row1, column=column1, padx=15, pady=5, sticky=W)


def measure_screen(text1, row1, column1):
    labal = Label(measurement_frame, text=text1, font=(
        "Arial", 15, ""), bg="grey", fg="black")
    labal.grid(row=row1, column=column1, padx=10, pady=5, sticky=E)


def save_bill():
    global bill_number
    if flore_Entry.get() == '' or wall_Entry.get() == '' or patta_Entry.get() == '' or molding_Entry.get() == '' or simple_molding_Entry.get() == '' or kithan_Entry.get() == '':
        messagebox.showerror("ERROR", "Values Are Required")
    else:
        result = messagebox.askyesno("Conform", "Do you want to save Bill")
        if result:
            bill_content = textarea.get(1.0, END)
            file = open(f'{bill_number}.txt', 'w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo(
                'Success', f'{bill_number} is saved Successfully')
            bill_number = random.randint(500, 1000)


bill_number = random.randint(500, 1000)


def add():
    room = str(mesure_combobox.get())
    MFE1 = float(mesure_floar_Entry1.get())
    MFE2 = float(mesure_floar_Entry2.get())
    MWE1 = float(mesure_wall_Entry1.get())
    MWE2 = float(mesure_wall_Entry2.get())
    MFE = float(mesure_patta_Entry.get())
    MME = float(mesure_molding_Entry.get())
    MSME = float(mesure_simple_molding_Entry.get())
    TMFE = MFE1 * MFE2
    TMWE = MWE1 * MWE2

    myconn = mysql.connector.connect(
        host="localhost", user="root", password="", database="shiv")

    cur = myconn.cursor()
    sql = "Insert into bill(room ,flore1 ,flore2 ,wall1 ,wall2 ,patta ,molding ,simple_molding ,flore ,wall ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (room, MFE1, MFE2, MWE1, MWE2, MFE, MME, MSME, TMFE, TMWE)
    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        messagebox.showerror("ERROR", "Not add data into database")
        myconn.rollback()

    messagebox.showinfo('Success', f'{cur.rowcount} row record inserted!')
    myconn.close()


def delete1():
    global deleteEntery
    DE = deleteEntery.get()

    myconn = mysql.connector.connect(
        host="localhost", user="root", password="", database="shiv")
    cur = myconn.cursor()
    sql = "DELETE From bill WHERE sr = %s"
    var = [DE]

    try:
        cur.execute(sql, var)
        myconn.commit()
    except:
        messagebox.showerror("ERROR", "Not delete data into database")
        myconn.rollback()

    messagebox.showinfo('Success', f'{cur.rowcount} row record deleted!')
    # print(cur.rowcount, "record deleted!")
    myconn.close()


def delete():

    global deleteEntery

    D = Tk()
    D.geometry("180x160")
    D.title("Delete")

    labal = Label(D, text="Select to Delete", font=("Arial", 15, "bold"))
    labal.grid(row=0, column=0, padx=5, pady=10)
    deleteEntery = Entry(D, font=("Arial", 15, "bold"), width=10)
    deleteEntery.grid(row=1, column=0, pady=10)
    delete_btn = Button(D, text="Delete", font=(
        "Arial", 15, "bold"), bg="red", fg="White", cursor="hand2", width=9, command=delete1)
    delete_btn.grid(row=2, column=0, padx=5, pady=10)

    D.mainloop()


def bill():
    global y

    myconn = mysql.connector.connect(
        host="localhost", user="root", password="", database="shiv")

    textarea.delete(1.0, END)
    textarea.insert(END, "\t\t\tKaran Tails Fitting")
    textarea.insert(
        END, "\n==================================================================")
    textarea.insert(
        END, "\n   Room \t\tFlore\t\tWall     Patta   Molding   Simple")
    textarea.insert(END, "\n  \t\t\t\t\t\t\t   Molding")
    mycursor = myconn.cursor()
    mycursor.execute("SELECT * from bill")
    myresult = mycursor.fetchall()
    for x in myresult:
        textarea.insert(
            END, f'\n {x[1]}  \t  {x[2]} x {x[3]}   {x[4]} x {x[5]} \t   {x[6]} \t  {x[7]}  \t  {x[8]}')

    textarea.insert(
        END, "\n==================================================================")
    my = myconn.cursor()
    my.execute(
        "SELECT sum(flore),sum(wall),sum(patta),sum(molding),sum(simple_molding) from bill")
    myresult = my.fetchall()
    for y in myresult:
        TFM = y[0]
        TWM = y[1]
        TPM = y[2]
        TMM = y[3]
        TSMM = y[4]
        textarea.insert(
            END, f'\n \t\t{int(TFM)}\t\t{int(TWM)}      {int(TPM)}      {int(TMM)}      {int(TSMM)}')
    textarea.insert(
        END, "\n==================================================================")

    myconn.close()

    FE = int(flore_Entry.get())
    WE = int(wall_Entry.get())
    PE = int(patta_Entry.get())
    ME = int(molding_Entry.get())
    SME = int(simple_molding_Entry.get())
    KE = int(kithan_Entry.get())

    TFE1 = FE * TFM
    TWE1 = WE * TWM
    TPE1 = PE * TPM
    TME1 = ME * TPM
    TSME1 = SME * TSMM
    TKE1 = kithan_Entry.get()
    TE1 = int(TFE1) + int(TWE1) + int(TPE1) + \
        int(TME1) + int(TSME1) + int(TKE1)

    textarea.insert(
        END, f'\n Flore             :     {TFM}   x  {FE}     =     {TFE1}')
    textarea.insert(
        END, f'\n Wall              :     {TWM}   x  {WE}     =     {TWE1}')
    textarea.insert(
        END, f'\n Patta             :     {TPM}   x  {PE}     =     {TPE1}')
    textarea.insert(
        END, f'\n Molding           :     {TMM}   x  {ME}     =     {TME1}')
    textarea.insert(
        END, f'\n Simple Molding    :    {TSMM}  x  {SME}     =     {TSME1}')
    textarea.insert(
        END, f'\n Kichan            :                         =     {TKE1}')
    textarea.insert(
        END, "\n==================================================================")
    textarea.insert(
        END, f'\n TOTAL             :                         =     {TE1}')

    TFE = total_flore_Entry.delete(0, END)
    TFE = total_flore_Entry.insert(END, f'{int(TFE1)}')
    TWE = total_wall_Entry.delete(0, END)
    TWE = total_wall_Entry.insert(END, f'{int(TWE1)}')
    TPE = total_patta_Entry.delete(0, END)
    TPE = total_patta_Entry.insert(END, f'{int(TPE1)}')
    TME = total_molding_Entry.delete(0, END)
    TME = total_molding_Entry.insert(END, f'{int(TME1)}')
    TSME = total_simple_molding_Entry.delete(0, END)
    TSME = total_simple_molding_Entry.insert(END, f'{int(TSME1)}')
    TKE = total_kithan_Entry.delete(0, END)
    TKE = total_kithan_Entry.insert(END, f'{int(TKE1)}')
    TE = total_Entry.delete(0, END)
    TE = total_Entry.insert(END, f'{int(TE1)}')


root = Tk()
root.geometry("1000x540")
root.title("Basic GUI")

titleframe = Frame(root, bd=3, relief=GROOVE, bg="grey")
titleframe.place(x=0, y=0, width=1000, height=40)

tl = Label(titleframe, text='Karan Tails Fitting', font=(
    "Arial", 20, "bold"), bg="grey", fg="red")
tl.pack()

mainframe = Frame(root, bd=3, relief=GROOVE, bg="grey")
mainframe.place(x=0, y=40, width=1000, height=90)

main("Flore :", 0, 0)
flore_Entry = Entry(mainframe, font=("Arial", 15, "bold"), width=10)
flore_Entry.grid(row=0, column=1, sticky=W)

main("Wall : ", 1, 0)
wall_Entry = Entry(mainframe, font=("Arial", 15, "bold"), width=10)
wall_Entry.grid(row=1, column=1, sticky=W)

main("Patta : ", 0, 2)
patta_Entry = Entry(mainframe, font=("Arial", 15, "bold"), width=10)
patta_Entry.grid(row=0, column=3, sticky=W)

main("Molding : ", 1, 2)
molding_Entry = Entry(mainframe, font=("Arial", 15, "bold"), width=10)
molding_Entry.grid(row=1, column=3, sticky=W)

main("Simple Molding : ", 0, 4)
simple_molding_Entry = Entry(mainframe, font=("Arial", 15, "bold"), width=10)
simple_molding_Entry.grid(row=0, column=5, sticky=W)

main("Kichan : ", 1, 4)
kithan_Entry = Entry(mainframe, font=("Arial", 15, "bold"), width=10)
kithan_Entry.grid(row=1, column=5, sticky=W)


# Measurement Entry
measurement_frame = Frame(root, bd=3, relief=GROOVE, bg="grey")
measurement_frame.place(x=0, y=130, width=1000, height=250)

mesure = ["Select", "one   ", "two   ", "three ", "four  ",
          "five  ", "six   ", "seven ", "eight ", "nine   ", "ten   "]

mesure_combobox = Combobox(measurement_frame, value=mesure, font=(
    "Arial", 10, "bold"), width=20, state="readonly")
mesure_combobox.current(0)
mesure_combobox.grid(row=0, column=1, sticky=W, padx=10, pady=10, columnspan=3)

labal = Label(measurement_frame, text="FLORE : ", font=(
    "Arial", 15, ""), bg="grey", fg="black")
labal.grid(row=1, column=0, padx=10, pady=5, sticky=E)

mesure_floar_Entry1 = Entry(measurement_frame, width=8)
mesure_floar_Entry1.grid(row=1, column=1, sticky=E)
mesure_floar_Entry1.insert(0, 0)

labal = Label(measurement_frame, text="X", font=(
    "Arial", 15, ""), bg="grey", fg="black")
labal.grid(row=1, column=2)

mesure_floar_Entry2 = Entry(measurement_frame, width=8)
mesure_floar_Entry2.grid(row=1, column=3, sticky=W)
mesure_floar_Entry2.insert(0, 0)

measure_screen("WALL : ", 2, 0)
mesure_wall_Entry1 = Entry(measurement_frame, width=8)
mesure_wall_Entry1.grid(row=2, column=1, sticky=E)
mesure_wall_Entry1.insert(0, 0)

labal = Label(measurement_frame, text="X", font=(
    "Arial", 15, ""), bg="grey", fg="black")
labal.grid(row=2, column=2)

mesure_wall_Entry2 = Entry(measurement_frame, width=8)
mesure_wall_Entry2.grid(row=2, column=3, sticky=W)
mesure_wall_Entry2.insert(0, 0)

measure_screen("PATTA : ", 3, 0)
mesure_patta_Entry = Entry(measurement_frame, width=23)
mesure_patta_Entry.grid(row=3, column=1, columnspan=3)
mesure_patta_Entry.insert(0, 0)

measure_screen("MOLDING : ", 4, 0)
mesure_molding_Entry = Entry(measurement_frame, width=23)
mesure_molding_Entry.grid(row=4, column=1, columnspan=3)
mesure_molding_Entry.insert(0, 0)

measure_screen("SIMPLE MOLDING : ", 5, 0)
mesure_simple_molding_Entry = Entry(measurement_frame, width=23)
mesure_simple_molding_Entry.grid(row=5, column=1, columnspan=3)
mesure_simple_molding_Entry.insert(0, 0)


# Bill Area
billarea = LabelFrame(measurement_frame, text="BIll Area", font=(
    "Arial", 10, "bold"), bg="white", fg="red", padx=5, pady=5)
billarea.place(x=410, y=10, width=570, height=220)

scroll_y = Scrollbar(billarea, orient=VERTICAL)
textarea = Text(billarea, yscrollcommand=scroll_y.set,
                bg="white", fg="black",)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=1)


# Total frame
total_frame = Frame(root, bd=3, relief=GROOVE, bg="grey")
total_frame.place(x=0, y=380, width=1000, height=160)

total1("Flore Total:", 0, 0)
total_flore_Entry = Entry(total_frame, width=10)
total_flore_Entry.grid(row=0, column=1, sticky=W)
total_flore_Entry.insert(0, 0)

total1("Wall Total: ", 1, 0)
total_wall_Entry = Entry(total_frame, width=10)
total_wall_Entry.grid(row=1, column=1, sticky=W)
total_wall_Entry.insert(0, 0)

total1("Patta Total: ", 2, 0)
total_patta_Entry = Entry(total_frame, width=10)
total_patta_Entry.grid(row=2, column=1, sticky=W)
total_patta_Entry.insert(0, 0)

total1("Molding Total: ", 0, 2)
total_molding_Entry = Entry(total_frame, width=10)
total_molding_Entry.grid(row=0, column=3, sticky=W)
total_molding_Entry.insert(0, 0)

total1("Simple Molding Total: ", 1, 2)
total_simple_molding_Entry = Entry(total_frame, width=10)
total_simple_molding_Entry.grid(row=1, column=3, sticky=W)
total_simple_molding_Entry.insert(0, 0)

total1("Kichan Total: ", 2, 2)
total_kithan_Entry = Entry(total_frame, width=10)
total_kithan_Entry.grid(row=2, column=3, sticky=W)
total_kithan_Entry.insert(0, 0)

total1("Total : ", 3, 1)
total_Entry = Entry(total_frame, width=20)
total_Entry.grid(row=3, column=2, sticky=W, rowspan=2)
total_Entry.insert(0, 0)


# Buttons
add_btn = Button(total_frame, text="Add", font=(
    "Arial", 15, "bold"), bg="red", fg="White", cursor="hand2", width=9, command=add)
add_btn.grid(row=0, column=4, rowspan=2, padx=20, pady=5)


New_btn = Button(total_frame, text="Delete", font=(
    "Arial", 15, "bold"), bg="red", fg="White", cursor="hand2", width=9, command=delete)
New_btn.grid(row=2, column=5, rowspan=2, padx=5, pady=5)

print_btn = Button(total_frame, text="Bill", font=(
    "Arial", 15, "bold"), bg="red", fg="White", cursor="hand2", width=9, command=bill)
print_btn.grid(row=0, column=6, rowspan=2, padx=20, pady=5)

New_btn = Button(total_frame, text="Print", font=(
    "Arial", 15, "bold"), bg="red", fg="White", cursor="hand2", width=9, command=save_bill)
New_btn.grid(row=2, column=6, rowspan=2, padx=5, pady=5)

root.mainloop()
