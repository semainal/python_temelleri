
SemaHesap = {
    "ad": "Sema İnal",
    "hesapNo": "223654",
    "bakiye": 10000,
    "ekHesap": 5000}

def bankamatik(hesap):
    print(f"Hoşgeldiniz {hesap['ad']}")
bankamatik(SemaHesap) 

toplam = SemaHesap["bakiye"] + SemaHesap["ekHesap"]
cekilentutar = input("Ne kadar çekmek istiyorsunuz?: ")
def paraCek(miktar):
    cekilentutar
    if SemaHesap["bakiye"] > miktar:
        SemaHesap["bakiye"] -= miktar
        print("Paranızı çekebilirsiniz.")  
        bakiyeSorgula(SemaHesap)
    
    else:
        print("Yetersiz Bakiye")
    















def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz: {hesap['ekHesap']} TLdir.")



bakiyeSorgula(SemaHesap)                 
                
  

