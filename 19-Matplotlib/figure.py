import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,9,20)
y = x **3
z = x**2

# kendimiz bütün grafiği çizebiliriz. hem axisi hem figure ü biz belirleyebiliriz.

"""
# axes = figure.add_axes([0.0,0.0,0.9,0.9]) # yüzey tabanı için ölçü verdik.
figure = plt.figure()

# 2 grafik iç içe çiziyoruz. biri büyük biri küçük.
axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])

axes_cube.plot(x,y, "y")
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.2,0.6,0.2,0.2])
axes_square.plot(x,z, color='green')
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.set_title("Square")
"""

"""
# 2 çizgiyi tek grafik üzerinde göstermek için:
figure = plt.figure()

axes = figure.add_axes([0,0,1,1]) # tam ekran grafik

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=2) # location: 1= sağ üst, 2= sol üst, 3= sol alt, 4= sağ alt
"""


# subplots - düzlemin boyutunu ayarlamak için:
fig, axes = plt.subplots(nrows=2,ncols=1,figsize = (4,4)) # 2 satır 1 kolon
axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure1.png") # klasör altına png dosyası olarak kaydedildi.
fig.savefig("figure1.pdf") # pdf olarak kaydetti



plt.show()
