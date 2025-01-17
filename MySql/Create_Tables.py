import mysql.connector

# Creating a Tables

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# Show Tables

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)


# Creating a new Column

mycursor = mydb.cursor()

mycursor.execute(
    "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
