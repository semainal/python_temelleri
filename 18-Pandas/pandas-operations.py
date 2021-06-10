import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcae","ade","cb","dea"]    
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal2 = lambda x: x*x 

result = df
result = df["Column2"].unique() # tekrarlayan elemanları 1 kere gösterir.
result = df["Column2"].nunique() # kaç sayı tekrarlamıyor onu verir. n => number
result = df["Column2"].value_counts() # her sayıdan kaç tane var onu verir.
result = df["Column1"] *2
result = df["Column1"].apply(kareal) # yukardaki 2 ile çaprma işlemi yerine,
# bir fonksiyon oluşturup apply(fonksiyon) yapabilirim.
result = df["Column1"].apply(kareal2)
result = df["Column1"].apply(lambda x: x*x)
result = df["Column3"].apply(len) # hangi elemanın kaç karakter uzunluğunda olduğunu verir.
df["Column4"] = df["Column3"].apply(len) # column4 üzerinden kaç karakter olduğunu gösterebiliriz. 
# print(df)
result = df.columns # kolonların isimleri gelir. kaç kolon var
result = len(df.columns) # kaç kolon var sayısı yazar
result = df.index # kaçtan başlayıp kaça gidiyor- satır
result = len(df.index) # kaç elemanlı olduğunu gösterir
result = df.info


result = df.sort_values("Column2") # kolon2 sıralı bir şekilde gelir
result = df.sort_values("Column3") # kolon 3 alfaberik şekilde gelir.
result = df.sort_values("Column1", ascending= False) # azalan şekilde gelir. diğerleri artan şekilde geliyordu.


data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)
df = df.pivot_table(index= "Ay", columns= "Kategori", values ="Gelir")
print(df)


# print(result)