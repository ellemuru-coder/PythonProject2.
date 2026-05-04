
# Vuodenajat monikkona 1–12
vuodenajat = (
    "talvi",  # 1
    "talvi",  # 2
    "kevät",  # 3
    "kevät",  # 4
    "kevät",  # 5
    "kesä",   # 6
    "kesä",   # 7
    "kesä",   # 8
    "syksy",  # 9
    "syksy",  # 10
    "syksy",  # 11
    "talvi"   # 12
)

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print("Vuodenaika on:", vuodenajat[kuukausi - 1])
else:
    print("Virheellinen kuukauden numero.")

nimet = set()

while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nSyötetyt nimet:")
for n in nimet:
    print(n)

lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Lisää uusi lentoasema")
    print("2 = Hae lentoaseman nimi ICAO-koodilla")
    print("3 = Lopeta")

    valinta = input("Valinta: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        print("Lopetetaan ohjelma.")
        break
    else:
        print("Virheellinen valinta.")