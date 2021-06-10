import pandas as pd


data = pd.read_csv("nba.csv")

data.dropna(inplace = True) # nan değerler orginalinden gitti.

data["Name"] = data["Name"].str.upper() # isimlerin hepsi büyük harf oldu.
data["Name"] = data["Name"].str.lower() # küçük harf
data["index"] = data["Name"].str.find("a") # yeni kolon açıp içinde a olanları buluyor.
data = data.Name.str.contains("Jordan") # True-false döner
data = data[data.Name.str.contains("Jordan")] # Jordan olan tün kayıtları döner.
data = data.Team.str.replace(" ", "-") # team içindeki tüm boşluk karakterlere - işaretini koydu
data = data.Team.str.replace(" ", "-").str.replace("*"," ") # üsttekinin devamı, bulduğu tüm * karakterlerinin yerine boşuk bırakır.
data[["First Name","Last Name"]] = data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True) # name kolonunu önce 2ye böldük, 
# sonra boşluk sayısını kontrol ettik, sonra first ve last name olarak yerleştirdik.





# print(data.columns)
print(data.head(10))
# print(data)
