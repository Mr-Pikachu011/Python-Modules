import mysql.connector

# Select a Multiple data at a time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="management"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM information")

myresult = mycursor.fetchall()

for x in myresult:
    print(x[1])


# Select Perticular data from tables

# mycursor = mydb.cursor()

# mycursor.execute("SELECT name, address FROM information")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x[1])


# Select only one Row of data

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()

# print(myresult)
