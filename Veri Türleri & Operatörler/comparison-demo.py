#1 Girilen 2 sayıdan hangisi büyüktür?

# a = int(input("sayı1: "))
# b = int(input("sayı2: "))

# result = (a > b)
# print(f"a: {a} b: {b} den büyüktür: {result}")

# result = (b > a)
# print(f"b: {b} a: {a} dan büyüktür: {result}")

#2 Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız.
#Eğer ortalama 50 ve üstündeyse "geçti", altındaysa "kaldı" yazdırın.


# x = float(input("vize1: "))
# y = float(input("vize2: "))
# z = float(input("final1: "))

# ort = ((x+y)/2*0.60)+(z*0.40)

# print(f"Not ortalamanız: {ort} ve dersten geçme durumunuz: {ort>=50}")


#3 Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# sayi = int(input("sayı: "))
# tekcift = (sayi %2 == 0)

# print(f"Girilen sayının çift olma durumu: {tekcift}")

#4 Girilen bir sayının negatif pozitif durumunu yazınız.

# sayi = float(input("sayı: "))

# negatif = sayi<0
# print(f"Girilen sayı: {sayi} negatiftir {negatif} ")

#5 Parola ve e-mail bilgisini isteyip doğruluğunu kontrol ediniz.
#(email: semainal35@gmail.com parola:12345)

email = "semainal35@gmail.com"
password = "12345"

# result = (input("email: ") == email)
# result = (input("password: ") == password)

# print(result)

girilenEmail = input("email: ")
girilenPassword = input("password: ")

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower().strip())

print(f"Email bilgisi doğru mu: {isEmail} ve girilen password doğru mu: {isPassword}.")