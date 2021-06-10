
import pandas as pd


df = pd.read_csv("nba.csv")


# 1- İlk 10 kaydı getiriniz.

result = df.head(10)

# 2- Toplam kaç kayıt vardır?

result = len(df.index)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir?

result = df["Salary"].sum() # toplam maaş
result = len(df.Name) # toplam kişi sayısı 458
result = df["Salary"].isnull() # nan değerler 
result = df["Salary"].isnull().sum() # nan değerler toplamı 12
result = df.dropna(subset=["Salary"], how="any")


def ortalama(df):
    toplam = df["Salary"].sum()
    adet= len(df.dropna(subset= ["Salary"], how="any"))
    return toplam / adet

result = ortalama(df)

# 4- En yüksek maaşı ne kadardır?

result = df["Salary"].max()


# 5- En yüksek maaşı alan oyuncu kimdir?

result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takım nedir?

result = df.query("Age >=20 & Age <=25")
result = df[(df["Age"] >=20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age",ascending=False) # alternatif

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir?

result = df[df["Name"] == "John Holland"]["Team"].iloc[0]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir?

result = df.groupby("Team")["Salary"].mean()

# 9- Kaç farklı takım mevcut?

result = len(df.groupby("Team"))
result = df["Team"].nunique()

# 10- Her takımda kaç oyuncu oynamaktadır?

result = df["Team"].value_counts()


# 11- İsmi içinde "and" geçen kayıtları bulunuz.
# result = df.dropna() # yada:
df.dropna(inplace=True)

# result = df[df["Name"].str.contains("and")].sort_values("Salary", ascending=False)

def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)]

print(result)