
def bilgileri_oku():
    with open("hasta_kayit.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(boykilo_indeksi(satir))


def boykilo_indeksi(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    hastaAdi = liste[0]
    boykilo = liste[1].split(",")

    boy = float(boykilo[0])
    kilo = float(boykilo[1])

    ortalama = kilo / (boy**2)

    if ortalama >= 30.0:
        deger = "Şişman (Obez)"

    elif ortalama >= 25.0:
        deger = "Fazla Kilolu"

    elif ortalama >= 18.5:
        deger = "Normal"

    else:
        deger = "Zayıf"    

    return hastaAdi+":"+deger+"\n"    


def hasta_bilgileri():
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    boy = input("Boy: ")
    kilo = input("Kilo: ")
    


    with open("hasta_kayit.txt", "a", encoding="utf-8") as file:
        file.write(isim+" "+soyisim+ ":" +boy+ "," +kilo+"\n")





def kaydet():
    with open("hasta_kayit.txt", "r", encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(boykilo_indeksi(i))

            with open("hasta_sonuclar.txt", "a", encoding="utf-8") as file2:
                for i in liste:
                    file2.write(i)


while True:
    
    islem = input("1- Hasta Bilgileri\n2- Boy/Kilo Endeksi\n3- Bilgileri Kayıt Et\n4- Çıkış\n")

    if islem == "1":
        hasta_bilgileri()

    elif islem == "2":
        bilgileri_oku()

    elif islem == "3":
        kaydet()

    else:
        break


