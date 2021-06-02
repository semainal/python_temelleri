#1
# name = input("İsim: ")
# age = int(input("Yaş: "))
# edu = input("Eğitim Durumu: ")



# if (age >= 18) and (edu == "lise" or edu == "üniversite"):
#  print("Ehliyet alabilirsiniz.")

# else:
#  print("Ehliyet alamazsınız.")

#2

sozlu1 = int(input("Sözlü1: "))
sozlu2 = int(input("Sözlü2: "))
yazili = int(input("Yazılı: "))

ort = ((sozlu1 + sozlu2)/2)*0.50 + (yazili*0.50)

if 85<= ort < 100:
 print("Notunuz 5")

elif 70<= ort < 84:
 print("Notunuz 4")

elif 55<=ort <69:
 print("Notunuz 3")

elif 45<= ort < 54:
 print("Notunuz 2")

elif 25<= ort<44:
 print("Notunuz 1")

else:
 print("Notunuz 0")



#3


# if days <= 365:
#  print("1.servis aralığı")
# elif  (days>365) and (days<= 730):
#  print("2.servis aralığı")
# elif (days>730) and  (days<= 1095):
#  print("3.servis aralığı")
# else:
#  print("Aracınızın garanti süresi dolmuş.")


#4

# x = int(input("Sayı: "))

# if x>0 and x%2==0:
#  print("Sayınız pozitif çift sayıdır.")

# else:
#  print("Sayınız pozitif çift sayı değildir.")

#5

# username = input("Kullanıcı adı: ")
# password = input("Şifre: ")

# if username == "semainal" and password== "1234":
#  print("Giriş Başarılı")


# else:
#  print("Kullanıcı bilgileriniz yanlış.")


#6

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a>b and a>c:
#  print("a en büyüktür.")

# elif b>a and b>c:
#  print("b en büyüktür.")

# elif c>a and c>b:
#  print("c en büyüktür.")

#7

# vize1 = int(input("vize1: "))
# vize2 = int(input("vize2: "))
# final = int(input("final: "))

# ort = ((vize1+vize2)/2) * 0.60 + final * 0.40

# if ort >= 50: 
#  print("Dersten başarıyla geçtiniz.")
# elif final >= 70:
#  print("Dersten başarıyla geçtiniz.")
# elif final<=50:
#  print("Final notunuz 50'nin altında olduğu için kaldınız.")


#8

# name = input("İsim: ")
# kg = float(input("Kilo: "))
# hg =float(input("Boy: "))

# formul = (kg)/ (hg**2)


# if (formul>=30.0) and (formul<=34.9):
#  print("Şişman (obez)")

# elif (formul>=25.0) and (formul >=29.9):
#  print("Fazla Kilolu")

# elif (formul>=18.5) and (formul >= 24.9):
#  print("Normal")

# elif (0 <= formul) and (formul >= 18.4):
#  print("Zayıf")

# else:
#  print("Bilgileriniz yanlış.")
