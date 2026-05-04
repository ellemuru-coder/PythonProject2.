# -----------------------------
# TEHTÄVÄ 9 — AUTO-LUOKKA
# -----------------------------

import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


# -----------------------------
# TEHTÄVÄN ALKUOSA (perusauton testaus)
# -----------------------------

auto = Auto("ABC-123", 142)

print("\nPerusauton tiedot:")
print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus)
print("Nopeus:", auto.nopeus)
print("Kuljettu matka:", auto.kuljettu_matka)

# Kiihdytykset
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print("\nNopeus kiihdytysten jälkeen:", auto.nopeus)

# Hätäjarrutus
auto.kiihdytä(-200)
print("Nopeus hätäjarrutuksen jälkeen:", auto.nopeus)


# -----------------------------
# TEHTÄVÄ 9 — AUTOKILPAILU
# -----------------------------

# Luodaan 10 autoa
autot = []

for i in range(1, 11):
    rek = f"ABC-{i}"
    huippu = random.randint(100, 200)
    auto = Auto(rek, huippu)
    autot.append(auto)

# Kilpailu jatkuu kunnes jokin auto saavuttaa 10 000 km
kilpailu_jatkuu = True

while kilpailu_jatkuu:

    # Tunnin välein tehdään nopeuden muutos ja ajo
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_jatkuu = False

# Lopuksi tulostetaan kaikki tulokset taulukkona
print("\nKILPAILUN LOPPUTULOKSET:")
print("Rekisteri | Huippu | Nopeus | Kuljettu matka")

for auto in autot:
    print(f"{auto.rekisteritunnus:8} | "
          f"{auto.huippunopeus:6} km/h | "
          f"{auto.nopeus:6} km/h | "
          f"{auto.kuljettu_matka:.1f} km")