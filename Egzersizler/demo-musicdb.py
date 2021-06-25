import mysql.connector
from mysql.connector import connection

# mydb = mysql.connector.connect(host = "localhost", user = "root", password = "Sema_tolga85")
# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE musicdb")

# print(mydb)

def insertMusic(name, singer, year, description):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "Sema_tolga85", database = "musicdb")
    cursor = connection.cursor()
    
    sql = ("INSERT INTO music(name,singer,year,description) VALUES (%s,%s,%s,%s)")
    values = (name, singer, year, description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapatılıyor..")





def insertMusics(list):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "Sema_tolga85", database = "musicdb")
    cursor = connection.cursor()
    
    sql = ("INSERT INTO music(name,singer,year,description) VALUES (%s,%s,%s,%s)")
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapatılıyor..")


list = []

while True:
    name = input("Şarkı adı: ")
    singer = input("Şarkıcı: ")
    year = float(input("Senesi: "))
    description = input("Açıklama: ")
    list.append((name,singer,year,description))

    result = input("Devam etmek istiyor musunuz? (E/H)")
    if result == "H":
        print("Database aktarımı yapılıyor...")
        print(list)
        insertMusics(list)
        break

