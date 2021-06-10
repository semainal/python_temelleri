import pandas as pd

df = pd.read_csv("nba.csv")
result = df
# 1- İlk 10 kaydı getiriniz.

result = df.head(10)
# 2- Toplam kaç kayıt vardır ?

result = len(df.index)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?

result = df["Salary"].mean()

# 4- En yüksek maaşı ne kadardır ?

result = df["Salary"].max()

# 5- En yüksek maaşı alan oyuncu kimdir ?

result = df[df["Salary"]== df["Salary"].max()]["Name"]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.

result = df.sort_values("Age", ascending=False).query("Age >=20 & Age <=25")[["Name","Team"]]

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?

result = df[df.Name.str.contains("John Holland")== True]["Team"]


# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?

result = df.groupby("Team")["Salary"].mean()

# 9- Kaç farklı takım mevcut ?

result = len(df.groupby("Team"))

# 10- Her takımda kaç oyuncu oynamaktadır ?

result = df.groupby("Team")["Name"].count()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.

result = df[df["Name"].str.contains("and")== True]["Name"]

print(result)