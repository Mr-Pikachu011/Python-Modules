import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="mydatabase"
# )

# mycursor = mydb.cursor()

# # mycursor.execute(
# #     "CREATE TABLE Vinay(name VARCHAR(255), address VARCHAR(255),age INT,persent INT)")

# # ql = "INSERT INTO Vinay (name, address,age,persent) VALUES (%s, %s,%s,%s)"
# # val = [
# #     ('Peter', 'Lowstreet 4', 10, 90),
# #     ('Amy', 'Apple st 652', 40, 60),
# #     ('Hannah', 'Mountain 21', 50, 50)
# # ]


# mycursor = mydb.cursor()
# mycursor.execute("SELECT sum(age),sum(persent) from Vinay")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x[0]*2, x[1]*2)
#     # for i in x:
#     # print(i[0]*3, '  And  ', i[1]*2)
#     # print(i[0])


myconn = mysql.connector.connect(
    host="localhost", user="root", password="", database="shiv")

# cur = myconn.cursor()
# sql = "Insert into bill(room ,flore1 ,flore2 ,wall1 ,wall2 ,patta ,molding ,simple_molding ,flore ,wall ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# val = (room, MFE1, MFE2, MWE1, MWE2, MFE, MME, MSME, TMFE, TMWE)
# sql = "Select * From bill"

# try:
#     cur.execute(sql)
#     myconn.commit()
# except:
#     print("not execute")
#     myconn.rollback()
# print(cur.rowcount, "record inserted!")


# mycursor = myconn.cursor()
# mycursor.execute("SELECT * from bill")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x[0], x[1], x[2], "x", x[3], x[4], "x", x[5], x[6], x[7], x[8])
#     # for i in x:
#     # print(i[0]*3, '  And  ', i[1]*2)
#     # print(i[0])
# myconn.close()\\


my = myconn.cursor()
my.execute(
    "SELECT sum(flore),sum(wall),sum(patta),sum(molding),sum(simple_molding) from bill")
myresult = my.fetchall()
for x in myresult:
    print(x[0], x[1], x[2], x[3], x[4])
myconn.close()
