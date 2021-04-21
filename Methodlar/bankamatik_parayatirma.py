SemaHesap = {
    "ad": "Sema İnal",
    "hesapNo": "123354",
    "bakiye": 0,
    "ekHesap": 1000}



def greeting(hesap):
    print("Hoşgeldiniz", hesap["ad"])

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Tek Hesabınızda {hesap['ekHesap']} TL bulunmaktadır.")


greeting(SemaHesap)
tercih = input("Ne işlem yapmak istiyorsunuz? (çekme / yatırma)")
    


if tercih == "yatırma":
    tutar= float(input("Ne kadar para yatırmak istiyorsunuz?: "))

    if SemaHesap["ekHesap"] <= 5000:
        if tutar < 5000-SemaHesap["ekHesap"]:
            SemaHesap["ekHesap"] += tutar
        
        elif tutar > 5000-SemaHesap["ekHesap"]:
            miktar = 5000-SemaHesap["ekHesap"]
            SemaHesap["ekHesap"] += miktar
            fark = tutar - miktar
            SemaHesap["bakiye"] += fark


    
 
    bakiyeSorgula(SemaHesap)

