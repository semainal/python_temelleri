import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df =pd.DataFrame(data, index = ["a","c","e","f","h"], columns= ["Column1","Column2","Column3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["Column4"] = newColumn


result = df

result = df.drop("Column1", axis= 1) # kolon1 i sütun olarak siler
result = df.drop(["Column1","Column2"], axis= 1) # kolon1 ve kolon2 yi sütun olarak siler
result = df.drop("a", axis =0) # a satırını siler
result = df.drop(["a","b","h"], axis = 0)

result = df.isnull() # true-false döner. nan olanlar false döner.
result = df.notnull() # true-false döner. nan olanlar true döner.
result = df.isnull().sum() # her kolonda nan olan toplam kaç değer var onu döner.
result = df["Column1"].isnull().sum() # kolon1 deki toplam nan değrlerini verir.
result = df[df["Column1"].isnull()] # kolon1deki tüm nan lar gelir. diğer kolonları da yazdırır.
result = df[df["Column1"].isnull()]["Column1"] # sadece kolon1 ve sadece nan olanlar gelir.
result = df[df["Column1"].notnull()]["Column1"] # not null olan değerler yani sayılar gelir.

result = df.dropna() # axis = 0 => satıra göre nan olanları getirmez. sadece sayı olanları getirir.
result = df.dropna(axis = 1) # herhangi bir kolonda nan varsa onu bize getirmez.
result = df.dropna(how = "any") # herhangi bir nan değeri bulursa siler.
result = df.dropna(how = "all") # tüm satır nan sa gelmez.
result = df.dropna(subset = ["Column1","Column2"], how= "all") # 1 ve 2. kolonda nan değeri olmayanları getirir.
result = df.dropna(subset = ["Column1","Column2"], how= "any") # her hangi birinde nan varsa getirmez
result = df.dropna(thresh = 2) # en az 2 tane normal veri olması gerekir
result = df.dropna(thresh= 4) # en az 4 tane normal veri olması gerekir.

result = df.fillna(value= "no input") # nan değerler yerine no input yazar
result = df.fillna(value= 1) # nan değerlere 1 yazar


# nan olan değerler yerine ortalama vermek için:
result = df.sum() # kolonların hepsinin tek tek toplamın getirir
result = df.sum().sum() # tüm kolonların toplam halini getirir.
result = df.size # toplam elemanı getirir. (8*4) bir matrisimiz var şuan.
result = df.isnull().sum().sum() # sadece normal değer olan toplam eleman sayısı gelir.

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum() # toplam elemandan (32), nan elemanları (13) çıkartıyorum.
    return toplam / adet

result = df.fillna(value= ortalama(df))


print(result)
# print(df)