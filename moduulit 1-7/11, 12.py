# ---------------------------------------------------------
# TEHTÄVÄ 11 — PERIYTYMINEN (JULKAISUT JA AUTOT)
# ---------------------------------------------------------
from idlelib.rpc import request_queue


# -------- Julkaisu / Kirja / Lehti --------

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}, kirjoittaja {self.kirjoittaja}, {self.sivumaara} sivua")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}, päätoimittaja {self.paatoimittaja}")


# -------- Auto / Sähköauto / Polttomoottoriauto --------

class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu += self.nopeus * tunnit


class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akku = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, tankki):
        super().__init__(rekisteri, huippunopeus)
        self.tankki = tankki


# -------- Pääohjelma tehtävä 11 --------

print("\n--- JULKAISUT ---")
a1 = Lehti("Aku Ankka", "Aki Hyyppä")
a2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

a1.tulosta_tiedot()
a2.tulosta_tiedot()

print("\n--- AUTOT ---")
s = Sahkoauto("ABC-15", 180, 52.5)
p = Polttomoottoriauto("ACD-123", 165, 32.3)

s.kiihdyta(100)
p.kiihdyta(90)

s.kulje(3)
p.kulje(3)

print(f"Sähköauto {s.rekisteri} matkamittari: {s.kuljettu} km")
print(f"Polttomoottoriauto {p.rekisteri} matkamittari: {p.kuljettu} km")



# ---------------------------------------------------------
# TEHTÄVÄ 12 — ULKOISET API-RAJAPINNAT
# ---------------------------------------------------------

import request


# -------- 12 A: Chuck Norris vitsi --------

print("\n--- CHUCK NORRIS -VITSI ---")
vitsi_url = "https://api.chucknorris.io/jokes/random"
vitsi_data = requests.get(vitsi_url).json()
print(vitsi_data["value"])


# -------- 12 B: OpenWeather API --------
# HUOM! Lisää oma API-avain tähän:
API_KEY = "OMA_API_KEY_TAHAN"   # <-- VAIHDA

kaupunki = input("\nAnna paikkakunnan nimi: ")

