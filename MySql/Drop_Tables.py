import mysql.connector

# Drop Table commands

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

# delete table

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)


# Delete table if Table are Exist

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
