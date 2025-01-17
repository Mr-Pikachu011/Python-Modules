# For connecting Mysql And Python

# Download and install "MySQL Connector":

# C:\Users>python -m pip install mysql-connector-python


# Create Connection
# Start by creating a connection to the database.

# Use the username and password from your MySQL database:

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

if mydb.is_connected():
    print("Connection Success")
else:
    print("Connection Fail")

print(mydb)

mydb.close()
