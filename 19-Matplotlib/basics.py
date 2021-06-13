from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

"""
x = [1,2,3,4]
y = [1,4,9,16]


# matplotlib plot style yazıp arayabilirsin çeşitleri var..

# plt.plot(x,y, color= "red", linewidth = "5") # rengi kırmızı oldu ve kalınlaştı
# plt.plot(x,y, "--g") # çizgi çizgi yeşil grafik gelir.

# sıralama: [marker][line][color]
plt.plot(x,y, "o--g") #"o"-> marker "--"-> line "g"->color
plt.axis([0,6,0,20]) # ilk 0,6 x ekseni, 2.seri 0,20 ise y ekseni

plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
"""

"""
x = np.linspace(0,2,100)
plt.plot(x,x, label="linear", color="red")
plt.plot(x,x**2, label="quadratic", color= "yellow")
plt.plot(x,x**3, label="cubic", color="green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("simple plot")

plt.legend() #linear,quadratic ve cubiclerin grafik şekilleri belli olsun diye bunu veriyoruz.
"""

"""
x = np.linspace(0,2,100)
# fig,axs = plt.subplots(2) # 2 farklı grafik oluşturmak için


fig,axs = plt.subplots(3)
axs[0].plot(x,x, color = "red")
axs[0].set_title("linear")

axs[1].plot(x,x**2, color = "green")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3, color = "blue")
axs[2].set_title("cubic")

plt.tight_layout() # başlıklar içiçe geçmesin diye kulanıyoruz.
"""

"""
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2) # 2 satır 2 kolon
fig.suptitle("Grafik Başlığı")

axs[0,0].plot(x,x, color = "red")
axs[0,1].plot(x,x**2, color = "green")
axs[1,0].plot(x,x**3, color = "blue")
axs[1,1].plot(x,x**4,color = "yellow")
"""


import pandas as pd

df = pd.read_csv("nba.csv")

df = df.drop(["Number"], axis=1).groupby("Team").mean()
# df.plot(subplots = True) # alt başlıkların tek tek hepsinin ortalaması almak için true diyoruz.
df.head().plot(subplots = True)
plt.legend()



plt.show()