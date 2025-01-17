import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)


# not execute

# mycursor = mydb.cursor()

# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)



