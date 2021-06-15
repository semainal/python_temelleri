import mysql.connector
from mysql.connector import connection
from mysql.connector import cursor

# 1-Workbench IDE ile scholldb isminde bir database oluşturup Studdent tablosu ekleyiniz.
#Id, StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz.

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "Sema_tolga85",
#     database = "Scholldb"
# )

# mycursor = mydb.cursor()
# # mycursor.execute("CREATE DATABASE scholldb")
# mycursor.execute("CREATE TABLE Student(Id INT, StudentNumber VARCHAR(5), Name VARCHAR(45), Surname VARCHAR(50), Birthdate DATETIME, Gender CHAR(1))")


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sema_tolga85",
    database = "scholldb"
)

mycursor = connection.cursor()

mycursor.execute("Show Databases")

for i in mycursor:
    print(i)
