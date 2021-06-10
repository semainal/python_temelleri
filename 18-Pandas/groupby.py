import pandas as pd
import numpy as np


personeller = {
    'Çalışan': ["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    'Departman': ["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları"],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt':["Kadıköy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadıköy"],
    'Maaş':[5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)

result = df
result = df["Maaş"].sum() # tüm maaşları toplar
result = df.groupby("Departman").groups 
result = df.groupby(["Departman","Semt"]).groups

semtler = df.groupby("Semt")

# for name, group in semtler: #alternatifi => for name,group in df.groupby("Semt"):
#     print(name)
#     print(group)


# for name,group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadıköy") # semt kategorisinin altından sadece kadıköy gelir.
result = df.groupby("Departman").get_group("Bilgi İşlem") # departman kategorisinin altınfan sadece bilgi işlem gelir.
result = df.groupby("Departman").sum() #yaş ve maaşların toplamı gelir.
result = df.groupby("Departman").mean() # ortalamalar gelir
result = df.groupby("Departman")["Maaş"].mean() # sadece maaş ortlaması gelir.
result = df.groupby("Semt")["Yaş"].mean() # semtlere göre yaş ortalamaları gelir.
result = df.groupby("Semt")["Maaş"].mean() # semtlere göre maaş ortlaması gelir.
result = df.groupby("Semt")["Çalışan"].count() # semtlere göre çalışan sayısı gelir.
result = df.groupby("Departman")["Yaş"].max() # departmana göre yaşı max olan gelir.
result = df.groupby("Departman")["Maaş"].min() # departmana göre en düşük maaş
result = df.groupby("Departman")["Maaş"].max()["Muhasebe"] # muhasebe departmanındaki en yüksek maaş gelir.
result = df.groupby("Departman").agg(np.mean) # depatmana göre yaş ve maaş ortalamasını numpy ile aldık
result = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min]) # numpy ile tek işlemde farklı sonuçlar alabiliriz.
# departmanların maaşlarının toplama, ortalama, min ve max değerlerini tek satırda yazdırdık.
result = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min]).loc["Muhasebe"] # sadece muhasebe için



print(result)