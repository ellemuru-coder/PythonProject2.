
import random

lukumaara = int(input("Kuinka monta arpakuutiota heitetään? "))
summa = 0

for i in range(lukumaara):
    heitto = random.randint(1, 6)
    summa += heitto

print("Silmälukujen summa:", summa)



luvut = []

while True:
    syote = input("Syötä luku:(tyhjä lopettaa) ")
    if syote == "":
        break
    luvut.append(float(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)



luku = int(input("Syötä kokonaisluku: "))

if luku < 2:
    print("Luku ei ole alkuluku.")
else:
    on_alkuluku = True
    for i in range(2, luku):
        if luku % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")



kaupungit = []

for i in range(5):
    nimi = input("Syötä kaupungin nimi: ")
    kaupungit.append(nimi)

print("Kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)

