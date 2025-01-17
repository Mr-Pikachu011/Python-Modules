from tkinter import messagebox
import customtkinter
import mysql.connector


# customtkinter.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


def bill():
    global y

    myconn = mysql.connector.connect(
        host="localhost", user="root", password="", database="shiv")

    # textarea.insert(1.0, "hello")

    # textarea.delete(1.0, 1)
    textarea.insert(
        'end', "\t\t\tKaran Tails Fitting")
    textarea.insert(
        'end', "\n==================================================================")
    textarea.insert(
        'end', "\n   Room \t\tFlore\t\tWall     Patta   Molding   Simple")
    textarea.insert(
        "end", "\n  \t\t\t\t\t\t\t   Molding")

    mycursor = myconn.cursor()
    mycursor.execute("SELECT * from bill")
    myresult = mycursor.fetchall()
    for x in myresult:
        textarea.insert(
            'end', f'\n {x[1]}  \t  {x[2]} x {x[3]}   {x[4]} x {x[5]} \t   {x[6]} \t  {x[7]}  \t  {x[8]}')

    textarea.insert(
        'end', "\n==================================================================")
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
            'end', f'\n \t\t{int(TFM)}\t\t{int(TWM)}      {int(TPM)}      {int(TMM)}      {int(TSMM)}')

    textarea.insert(
        'end', "\n==================================================================")

    myconn.close()

    # FE = int(flore_Entry.get())
    # WE = int(wall_Entry.get())
    # PE = int(patta_Entry.get())
    # ME = int(molding_Entry.get())
    # SME = int(simple_molding_Entry.get())
    # KE = int(kithan_Entry.get())

    # TFE1 = FE * TFM
    # TWE1 = WE * TWM
    # TPE1 = PE * TPM
    # TME1 = ME * TPM
    # TSME1 = SME * TSMM
    # TKE1 = kithan_Entry.get()
    # TE1 = int(TFE1) + int(TWE1) + int(TPE1) + \
    #     int(TME1) + int(TSME1) + int(TKE1)

    # textarea.insert(
    #     1, f'\n Flore             :     {TFM}   x  {FE}     =     {TFE1}')
    # textarea.insert(
    #     1, f'\n Wall              :     {TWM}   x  {WE}     =     {TWE1}')
    # textarea.insert(
    #     1, f'\n Patta             :     {TPM}   x  {PE}     =     {TPE1}')
    # textarea.insert(
    #     1, f'\n Molding           :     {TMM}   x  {ME}     =     {TME1}')
    # textarea.insert(
    #     1, f'\n Simple Molding    :    {TSMM}  x  {SME}     =     {TSME1}')
    # textarea.insert(
    #     1, f'\n Kichan            :                         =     {TKE1}')
    # textarea.insert(
    #     1, "\n==================================================================")
    # textarea.insert(
    #     1, f'\n TOTAL             :                         =     {TE1}')

    # TFE = total_flore_Entry.delete(0, 1)
    # TFE = total_flore_Entry.insert(1, f'{int(TFE1)}')
    # TWE = total_wall_Entry.delete(0, 1)
    # TWE = total_wall_Entry.insert(1, f'{int(TWE1)}')
    # TPE = total_patta_Entry.delete(0, 1)
    # TPE = total_patta_Entry.insert(1, f'{int(TPE1)}')
    # TME = total_molding_Entry.delete(0, 1)
    # TME = total_molding_Entry.insert(1, f'{int(TME1)}')
    # TSME = total_simple_molding_Entry.delete(0, 1)
    # TSME = total_simple_molding_Entry.insert(1, f'{int(TSME1)}')
    # TKE = total_kithan_Entry.delete(0, 1)
    # TKE = total_kithan_Entry.insert(1, f'{int(TKE1)}')
    # TE = total_Entry.delete(0, 1)
    # TE = total_Entry.insert(1, f'{int(TE1)}')


def rate_add():
    # room = str(choice)
    FE = float(Flore_Entry.get())
    WE = float(wall_Entry.get())
    PE = float(patta_Entry.get())
    ME = float(molding_Entry.get())
    SME = float(simple_molding_Entry.get())
    KE = float(kichan_Entry.get())

    myconn = mysql.connector.connect(
        host="localhost", user="root", password="", database="shiv")

    cur = myconn.cursor()
    sql = "INSERT INTO rate (flore_rate,wall_rate,patta_rate,molding_rate,simple_molding_rate,kichan_rate) values (%s,%s,%s,%s,%s,%s)"
    val = (FE, WE, PE, ME, SME, KE)
    print()
    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        messagebox.showerror("ERROR", "Not add data into database")
        myconn.rollback()
    # mysqli_error(myconn)
    messagebox.showinfo('Success', f'{cur.rowcount} row record inserted!')
    myconn.close()


def add():
    # room = str(choice)
    MFE1 = float(Flore1_mesure_Entry.get())
    MFE2 = float(Flore2_mesure_Entry.get())
    MWE1 = float(wall1_mesure_Entry.get())
    MWE2 = float(wall2_mesure_Entry.get())
    MFE = float(patta_mesure_Entry.get())
    MME = float(molding_mesure_Entry.get())
    MSME = float(simple_molding_mesure_Entry.get())
    TMFE = MFE1 * MFE2
    TMWE = MWE1 * MWE2

    myconn = mysql.connector.connect(
        host="localhost", user="root", password="", database="shiv")

    cur = myconn.cursor()
    sql = "Insert into bill(flore1 ,flore2 ,wall1 ,wall2 ,patta ,molding ,simple_molding ,flore ,wall ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (MFE1, MFE2, MWE1, MWE2, MFE, MME, MSME, TMFE, TMWE)
    print()
    try:
        cur.execute(sql, val)
        myconn.commit()
    except:
        messagebox.showerror("ERROR", "Not add data into database")
        myconn.rollback()
    # mysqli_error(myconn)
    messagebox.showinfo('Success', f'{cur.rowcount} row record inserted!')
    myconn.close()


root = customtkinter.CTk()
root.title("Karan Tails Fitting")
root.geometry("600x350")


tabview = customtkinter.CTkTabview(master=root, width=570, height=330)
tabview.pack(padx=5, pady=5)


tabview.add("Profile")
tabview.add("Rate")
tabview.add("Mesurement")
tabview.add("Bill")
tabview.add("Setting")
tabview.set("Profile")


# ------------------------------------- Profile -------------------------------------

label1 = customtkinter.CTkLabel(master=tabview.tab("Profile"),
                                text="Karan Tails Fitting",
                                font=("Algerian", 30))
label1.pack(padx=20, pady=20)

label1 = customtkinter.CTkLabel(master=tabview.tab("Profile"))
label1.place(x=30, y=70)


# -------------------------------------  Rate  -------------------------------------

label = customtkinter.CTkLabel(master=tabview.tab("Rate"),
                               text="Flore : ",
                               padx=20, pady=25)
label.grid(row=1, column=1, sticky="e")
Flore_Entry = customtkinter.CTkEntry(master=tabview.tab("Rate"))
Flore_Entry.grid(row=1, column=2)

label = customtkinter.CTkLabel(master=tabview.tab("Rate"),
                               text="Wall : ",
                               padx=20, pady=25)
label.grid(row=1, column=3, sticky="e")
wall_Entry = customtkinter.CTkEntry(master=tabview.tab("Rate"))
wall_Entry.grid(row=1, column=4)

label = customtkinter.CTkLabel(master=tabview.tab("Rate"),
                               text="Patta : ",
                               padx=20, pady=25)
label.grid(row=2, column=1, sticky="e")
patta_Entry = customtkinter.CTkEntry(master=tabview.tab("Rate"))
patta_Entry.grid(row=2, column=2)

label = customtkinter.CTkLabel(master=tabview.tab("Rate"),
                               text="Molding : ",
                               padx=20, pady=25)
label.grid(row=2, column=3, sticky="e")
molding_Entry = customtkinter.CTkEntry(master=tabview.tab("Rate"))
molding_Entry.grid(row=2, column=4)

label = customtkinter.CTkLabel(master=tabview.tab("Rate"),
                               text="Simple Molding : ",
                               padx=20, pady=25)
label.grid(row=3, column=1, sticky="e")
simple_molding_Entry = customtkinter.CTkEntry(master=tabview.tab("Rate"))
simple_molding_Entry.grid(row=3, column=2)

label = customtkinter.CTkLabel(master=tabview.tab("Rate"),
                               text="Kichan : ",
                               padx=20, pady=25)
label.grid(row=3, column=3, sticky="e")
kichan_Entry = customtkinter.CTkEntry(master=tabview.tab("Rate"))
kichan_Entry.grid(row=3, column=4)

rate_button = customtkinter.CTkButton(master=tabview.tab("Rate"),
                                      text="Add", command=rate_add)
rate_button.grid(row=4, column=2, columnspan=3, pady=20)


# ------------------------------------- mesurement -------------------------------------

label = customtkinter.CTkLabel(master=tabview.tab("Mesurement"),
                               text="    ",
                               padx=55, pady=12)
label.grid(row=1, column=0, rowspan=6)

mesure = ["Select", "one   ", "two   ", "three ", "four  ",
          "five  ", "six   ", "seven ", "eight ", "nine   ", "ten   "]

label = customtkinter.CTkLabel(master=tabview.tab("Mesurement"),
                               text="Room : ",
                               padx=20, pady=12)
label.grid(row=0, column=1, sticky="e")
room = customtkinter.CTkComboBox(
    master=tabview.tab("Mesurement"), values=mesure)
room.grid(row=0, column=2, columnspan=3)

label = customtkinter.CTkLabel(master=tabview.tab("Mesurement"),
                               text="Float : ",
                               padx=20, pady=12)
label.grid(row=1, column=1, sticky="e")
Flore1_mesure_Entry = customtkinter.CTkEntry(
    master=tabview.tab("Mesurement"), width=50)
Flore1_mesure_Entry.grid(row=1, column=2)
label = customtkinter.CTkLabel(master=tabview.tab(
    "Mesurement"), text=" x ", font=("Arial", 25))
label.grid(row=1, column=3)
Flore2_mesure_Entry = customtkinter.CTkEntry(
    master=tabview.tab("Mesurement"), width=50)
Flore2_mesure_Entry.grid(row=1, column=4)

label = customtkinter.CTkLabel(master=tabview.tab("Mesurement"),
                               text="Wall   : ", padx=20, pady=12)
label.grid(row=2, column=1, sticky="e")
wall1_mesure_Entry = customtkinter.CTkEntry(
    master=tabview.tab("Mesurement"), width=50)
wall1_mesure_Entry.grid(row=2, column=2)
label = customtkinter.CTkLabel(master=tabview.tab("Mesurement"),
                               text=" x ", font=("Arial", 25))
label.grid(row=2, column=3)
wall2_mesure_Entry = customtkinter.CTkEntry(
    master=tabview.tab("Mesurement"), width=50)
wall2_mesure_Entry.grid(row=2, column=4)

label = customtkinter.CTkLabel(master=tabview.tab("Mesurement"),
                               text="Patta : ",
                               padx=20, pady=12)
label.grid(row=3, column=1, sticky="e")
patta_mesure_Entry = customtkinter.CTkEntry(master=tabview.tab("Mesurement"))
patta_mesure_Entry.grid(row=3, column=2, columnspan=3)

label = customtkinter.CTkLabel(master=tabview.tab("Mesurement"),
                               text="Molding : ",
                               padx=20, pady=12)
label.grid(row=4, column=1, sticky="e")
molding_mesure_Entry = customtkinter.CTkEntry(master=tabview.tab("Mesurement"))
molding_mesure_Entry.grid(row=4, column=2, columnspan=3)

label = customtkinter.CTkLabel(master=tabview.tab("Mesurement"),
                               text="Simple Molding : ",
                               padx=20, pady=12)
label.grid(row=5, column=1, sticky="e")
simple_molding_mesure_Entry = customtkinter.CTkEntry(
    master=tabview.tab("Mesurement"))
simple_molding_mesure_Entry.grid(row=5, column=2, columnspan=3)

add_button = customtkinter.CTkButton(master=tabview.tab("Mesurement"),
                                     text="Add", command=add)
add_button.grid(row=6, column=2, columnspan=3, pady=12)


# ------------------------------------- Bill area -------------------------------------

label = customtkinter.CTkLabel(master=tabview.tab("Bill"),
                               text="Search : ")
label.grid(row=1, column=1, padx=10, sticky="w")

search_Entry = customtkinter.CTkEntry(master=tabview.tab("Bill"))
search_Entry.grid(row=1, column=2, sticky="w")

search_button = customtkinter.CTkButton(master=tabview.tab("Bill"),
                                        text="Search")
search_button.grid(row=1, column=3, pady=10, padx=10, sticky="e")

textarea = customtkinter.CTkTextbox(master=tabview.tab("Bill"),
                                    height=180, width=540)
textarea.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

bill_button = customtkinter.CTkButton(master=tabview.tab("Bill"),
                                      text="Bill", width=540, command=bill)
bill_button.grid(row=3, column=1, columnspan=3)


# ------------------------------------- Setting -------------------------------------

def switch_event():
    if switch_var.get() == "on":
        customtkinter.set_appearance_mode("light")
    elif switch_var.get() == "off":
        customtkinter.set_appearance_mode("dark")


switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(master=tabview.tab("Setting"), text="Mode", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off").pack()


root.mainloop()
