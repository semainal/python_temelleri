import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns = ["Column1", "Column2", "Column3"])

#kolona göre seçmek için
result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]

#satıra göre seçmek için

# loc["row", "column"] => loc ["row"] => loc[":","column"]
result = df.loc["A"]
result = type(df.loc["A"])
result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column2"]]

#kolonları tek tek seçmek yerşne belli bir aralıkta seçmek için
result = df.loc[:,"Column1":"Column3"]

#başlangıcı belirtmeden
result = df.loc[:,:"Column3"]

#satır için

result = df.loc["A":"C", :"Column2"]
result = df.loc["A", :"Column2"]
result = df.loc["A", "Column2"]
result = df.loc[:"B", "Column2"]

#index'e göre seçim (şuan hata alırım çünkü index numaralarını belirttik)
#illa index'le çalışacağım diyorsan iloc kullanmalısın.

result = df.iloc[2]

result = df.loc[["A","B"],["Column1","Column2"]]

#yeni kolon eklemek için:
df["Column4"] = pd.Series(randn(3), ["A","B","C"])

df["Column5"] = df["Column1"] + df["Column3"]

#kolon silmek için:
# print(df.drop("Column5", axis = 1))
# inplace = True demezsen orjinal data üzerinde değişiklik olmaz
result = df.drop("Column5", axis = 1, inplace = True)
# result = df.drop("Column5", axis = 1, inplace = False)


print(result)
print(df)