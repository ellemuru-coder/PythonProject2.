
import random

def heita_noppaa():
    return random.randint(1, 6)

# pääohjelma
while True:
    tulos = heita_noppaa()
    print("Heitto:", tulos)
    if tulos == 6:
        break



import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

# pääohjelma
maksimi = int(input("Anna nopan maksimisilmäluku: "))

while True:
    tulos = heita_noppaa(maksimi)
    print("Heitto:", tulos)
    if tulos == maksimi:
        break


def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

# pääohjelma
while True:
    maara = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))
    if maara < 0:
        break

    litrat = gallonat_litroiksi(maara)
    print("Litroina:", litrat)


def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

# testipääohjelma
luvut = [3, 7, 2, 10, 5]
tulos = laske_summa(luvut)
print("Listan summa:", tulos)


def poista_parittomat(lista):
    tulos = []
    for luku in lista:
        if luku % 2 == 0:
            tulos.append(luku)
    return tulos

# testipääohjelma
alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8]
karsittu = poista_parittomat(alkuperainen)

print("Alkuperäinen lista:", alkuperainen)
print("Parilliset luvut:", karsittu)


import math

def pizzan_yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * sade_m ** 2
    return hinta / pinta_ala

# pääohjelma
d1 = float(input("Anna pizzan 1 halkaisija (cm): "))
h1 = float(input("Anna pizzan 1 hinta (€): "))

d2 = float(input("Anna pizzan 2 halkaisija (cm): "))
h2 = float(input("Anna pizzan 2 hinta (€): "))

yks1 = pizzan_yksikkohinta(d1, h1)
yks2 = pizzan_yksikkohinta(d2, h2)

if yks1 < yks2:
    print("Pizza 1 on parempi vastine rahalle.")
elif yks2 < yks1:
    print("Pizza 2 on parempi vastine rahalle.")
else:
    print("Pizzat ovat yhtä edullisia.")

