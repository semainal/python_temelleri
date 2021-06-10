import pandas as pd
import numpy as np


data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns= ["Column1","Column2","Column3","Column4","Column5"])

result = df

#data içinde kaç kolon var görmek için:
result = df.columns

#ilk 5 satır için:
result = df.head()
result = df.head(10)

#sondan 5 satır
result = df.tail()
result = df.tail(10)
result = df["Column1"].head() # sadece column1 ve ilk 5 satır gelir
result = df.Column1.head() # yukardakinin alternatifi
result = df[["Column1","Column2"]].head() # adı yazılan kolonlar ve ilk 5 satır gelir.
result = df[5:15][["Column1","Column2"]].head() #5-15 arası gelir ama head dediğim için 5 tanesi gelir.
result = df[5:15][["Column1","Column2"]].tail()

#filtreleme

result = df > 50 #true-false döner
result = df[result] # 50 üstü sayılar döner
result = df[df % 2 ==0]
result = df["Column1"] > 50
result = df[df["Column1"] > 50][["Column1","Column2"]] # column1 in 50den büyükleri, column2 nin aynı indexdeki sayıları gelecek
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] <= 70)] [["Column1","Column2"]]
result = df.query("Column1 >=50 & Column1 %2 ==0")[["Column1","Column2"]]
result = df.query("Column1 >=50 | Column2 %2 ==0")[["Column1","Column2"]]



print(result)