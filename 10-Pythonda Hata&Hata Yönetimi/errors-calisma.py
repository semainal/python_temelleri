# liste = ["1","2","5a","10b","abc","30","50"]

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue




# while True:
#     password = input("Password: ")
#     if password =="q":
#         break


#     try:
#         result = float(password)
#         print("Girdiğiniz sayı: ",result)
#         break
#     except ValueError:
#         print("Geçersiz sayı")
#         continue


turkce_karakter = "şçğüöıİ"

parola = input("parola: ")

for i in parola:
    if i in turkce_karakter:
        raise TypeError ("Türkçe karakter kullanmayınız.")
    else:
        pass
print("Geçerli parola")
