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


print(result)