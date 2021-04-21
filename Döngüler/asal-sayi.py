sayi = int(input("Bir sayı Giriniz: "))
asalMi = True

if sayi == 1:
 print("1 sayısı asal değildir.")

for i in range(2, sayi):
 if (sayi %i == 0):
    asalMi = False
    break

if asalMi:
 print("Asal sayıdır.")
else:
 print("Asal sayı değildir.")