# --------------------------------------------------
# TEHTÄVÄ 10 – HISSI JA TALO
# --------------------------------------------------

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.sijainti = alin_kerros

    def kerros_ylös(self):
        if self.sijainti < self.ylin:
            self.sijainti += 1
            print(f"Hissi on nyt kerroksessa {self.sijainti}")

    def kerros_alas(self):
        if self.sijainti > self.alin:
            self.sijainti -= 1
            print(f"Hissi on nyt kerroksessa {self.sijainti}")

    def siirry_kerrokseen(self, kohde):
        print(f"\nHissi siirtyy kerrokseen {kohde}...")
        while self.sijainti < kohde:
            self.kerros_ylös()
        while self.sijainti > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for _ in range(hissien_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissi_numero, kohdekerros):
        print(f"\nAjetaan hissiä {hissi_numero} kerrokseen {kohdekerros}")
        self.hissit[hissi_numero - 1].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        print("\n*** P A L O H Ä L Y T Y S ***")
        print("Kaikki hissit siirtyvät pohjakerrokseen!")
        for i, hissi in enumerate(self.hissit, start=1):
            print(f"\nHissi {i} siirtyy pohjakerrokseen:")
            hissi.siirry_kerrokseen(hissi.alin)


# --------------------------------------------------
# PÄÄOHJELMA – TESTAUS
# --------------------------------------------------

# Luodaan talo, jossa 3 hissiä ja kerrokset 1–10
talo = Talo(1, 10, 3)

# Testataan yhden hissin ajoa
talo.aja_hissia(1, 7)
talo.aja_hissia(1, 3)

# Palohälytys
talo.palohälytys()