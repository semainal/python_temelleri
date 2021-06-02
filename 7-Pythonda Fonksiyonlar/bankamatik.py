SemaHesap = {
    "ad": "Sema İnal",
    "hesapNo": "12345678",
    "bakiye": 15000,
    "ekHesap": 5000}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print(f"Paranızı çekebilirsiniz. ")
        bakiyeSorgula()
    
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek Hesap kullanılsın mı? (e/h)")

            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print(f"Paranızı Çekebilirsiniz. ")
                bakiyeSorgula(SemaHesap)
            else:
                print(f"{hesap['hesapNo']}nolu hesabınızda {hesap['bakiye']} bakiye bulunmaktadır.")
        else:
            print("Bakiye yetersiz.")
            bakiyeSorgula()


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']}TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(SemaHesap,16000)




