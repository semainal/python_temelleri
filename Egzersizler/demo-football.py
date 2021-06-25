
from typing import Tuple
import mysql.connector
from mysql.connector import connection
from mysql.connector.utils import NUMERIC_TYPES




def insertPlayer(name,surname,number,position):
    connection = mysql.connector.connect(host ="localhost", user ="root", password ="Sema_tolga85", database ="footballdb")
    cursor = connection.cursor()

    sql ="INSERT INTO players(name, surname, number, position) VALUES (%s,%s,%s,%s)"
    values = (name,surname,number,position)

    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı aktarılıyor...")

def insertPlayers(list):
    connection = mysql.connector.connect(host ="localhost", user ="root", password ="Sema_tolga85", database ="footballdb")
    cursor = connection.cursor()

    sql ="INSERT INTO players(name, surname, number, position) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()
        print("Database bağlantısı kapandi...")

list = []

while True:
    name = input("İsim: ")
    surname = input("Soyisim: ")
    number = int(input("Numarası: "))
    position = input("Pozisyonu: ")
    list.append((name,surname,number, position))

    result = input("Devam etmek istiyor musunuz? (e/h)")
    if result == "h":
        print("Database bağlantısı aktarılıyor...")
        print(list)
        insertPlayers(list)
        break






