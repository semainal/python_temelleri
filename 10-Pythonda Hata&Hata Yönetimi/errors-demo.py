
import re


liste = ["1", "2", "5a", "10b", "abc","10","50"]

#1
# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue


#2

# while True:
#     password = input("Şifre: ")
#     if password == "q":
#           break
#     try:
#         result = float(password)
#         print("Girdiğiniz sayı: ", result)
#             break
#     except ValueError:
#         print("Geçersiz Sayı.")
#         continue

        
#3

# turkce_karakterler = "şçğüöıİ"

# password = input("Password: ")

# for i in password:
#     if i in turkce_karakterler:
#         raise TypeError("Türkçe karakter kullanmayınız.")
#     else:
#         pass
# print("İşlem tamamlandı.")




def checkPassword(parola):
    turkce_karakterler = "şçöüğıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Türkçe karakter kullanmayınız.")
        else:
            pass
    print("İşlem tamamlandı.")

parola = input("parola: ")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)



#4


def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif değer.")
    result = 1


    for i in range (x, x+1):
        result *=i

    return result

for x in [5,10,20,"10a",-3]:
    try:
        y= faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)











         
  






    

