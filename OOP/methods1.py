class Circle:
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle()
c2 = Circle(5)

print(f"Dairenin alanı: {c1.alan_hesapla()} ve dairenin çevresi: {c1.cevre_hesapla()}")
print(f"Dairenin alanı: {c2.alan_hesapla()} ve dairenin çevresi: {c2.cevre_hesapla()}")