import numpy as np


class Auto:
    negy_kereke_van = True
    szamlalo = 0

    def __init__(self, szin, evjarat, futott_km, tipus):
        self.szin = szin
        self.evjarat = evjarat
        Auto.szamlalo += 1
        self.futott_km = futott_km
        self.tipus = tipus

    def kiir_szin(self):
        print(self.szin)

    def fut(self, ut):
        self.futott_km += ut

    def __str__(self):
        return "[Auto] szín: " + self.szin + "; evjarat: " + str(self.evjarat) + ";"

    def __add__(self, other):
        return self.futott_km + other.futott_km

auto_1 = Auto("Fekete", 2020, 0, "Kamion")
auto_2 = Auto("Piros", 2017, 100, "Autó")

print(auto_1.szin)
print(Auto.negy_kereke_van)

auto_1.kiir_szin()

print(auto_1.futott_km)

auto_1.fut(1000)

print(auto_1.futott_km)
print(auto_2.futott_km)
print(auto_1)
print(auto_1 + auto_2)
