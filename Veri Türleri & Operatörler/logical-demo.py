#1 Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# a = int(input("sayı: "))
# result = ((a>0) and (a<100))


#2 Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# a = int(input("sayı: "))
# result = ((a>0) and (a%2 == 0))

#3 email ve parola bilgileri ile giriş kontrolü yapınız.

# email = "semainal35@gmail.com"
# password = "12345"

# girilenEmail = input("email: ")
# girilenPassword = input("password: ")

# result = (girilenEmail == email) and (girilenPassword == password)


#4 Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input("sayı1: "))
# b = int(input("sayı2: "))
# c = int(input("sayı3: "))

# result = ((a>b) and (a>c)) 
# print(f"a en büyük sayıdır {result}")

# result = ((b>a) and (b>c)) 
# print(f"b en büyük sayıdır {result}")

# result = ((c>a) and (c>b)) 
# print(f"c en büyük sayıdır {result}")


#5 Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#Eğer ortalama 50 ve üzerindeyse geçti, değilse kaldı yazdırın.

# vize1 = float(input("Vize1: "))
# vize2 = float(input("vize2: "))
# final = float(input("Final: "))

# ortalama = (((vize1+vize2)/2)*0.60) + (final*0.40)

# result = ((ortalama >= 50) and (final>=50)) or (final>= 70)
# print(f"Not ortalamanız: {ortalama} ve dersten geçme durumu: {result}")

#6 Kişinin ad, kilo ve boy bilgilerini alıp kilo indeklesini hesaplayınız.
#Formül: (Kilo / boy uzunluğunun karesi)
#Aşağıdaki tabloya Göre kişi hangi gruba ait.
#0-18.4 => Zayıf
#18.5 - 24.9 =>Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)

# name = input("İsim: ")
# weight = input("Kilo: ")
# height = input("Boy: ")

# formul = (float(weight) / float(height)**2)

# zayıf = ((formul<= 18.4) and (formul>0))
# normal = (formul>=18.5) and (formul<=24.9)
# fazlaKilolu = ((formul>=25.0) and (formul<=29.9))
# sisman = ((formul>=30.0) and (formul<=34.9))

# print(f"Boy {height} ve Kilo {weight} indeksiniz: {formul} ve kilo değerlendirmeniz?:{zayıf} ")
# print(f"Boy {height} ve Kilo {weight} indeksiniz: {formul} ve kilo değerlendirmeniz?:{normal} ")
# print(f"Boy {height} ve Kilo {weight} indeksiniz: {formul} ve kilo değerlendirmeniz?:{fazlaKilolu} ")
# print(f"Boy {height} ve Kilo {weight} indeksiniz: {formul} ve kilo değerlendirmeniz?:{sisman} ")

