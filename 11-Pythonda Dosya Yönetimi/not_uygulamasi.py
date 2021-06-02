
def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")
    
    vize1 = int(notlar[0])
    vize2 = int(notlar[1])
    final = int(notlar[2])

    ortalama = int(((vize1 + vize2)/2) * 0.40) + int(final * 0.60)

    if ortalama >= 90:
        harf = "AA"
    elif ortalama >=85:
        harf = "BA"
    elif ortalama >=80:
        harf = "BB"
    elif ortalama >=75:
        harf = "CB"
    elif ortalama >=70:
        harf = "CC"
    elif ortalama >=65:
        harf = "DC"
    elif ortalama >=60:
        harf = "DD"
    elif ortalama >=50:
        harf = "DF"
    else:
        harf = "FF"

    return ogrenciAdi+ ":" +harf+ "\n"




def ortalamalari_oku():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input("Öğrenci Adı: ")
    soyad= input("Öğrenci Soyadı: ")
    vize1= input("Vize 1: ")
    vize2= input("Vize 2: ")
    final= input("Final: ")
    

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+vize1+","+vize2+","+final+"\n")

def notlari_kayitet():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))


        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)
    




while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n")

    if islem == "1":
        ortalamalari_oku()
    
    elif islem == "2":
        not_gir()

    elif islem == "3":
        notlari_kayitet()

    else:
        break