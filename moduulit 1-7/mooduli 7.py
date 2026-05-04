
vuodenajat = (
    "talvi",  # joulukuu
    "talvi",  # tammikuu
    "talvi",  # helmikuu
    "kevät",  # maaliskuu
    "kevät",  # huhtikuu
    "kevät",  # toukokuu
    "kesä",   # kesäkuu
    "kesä",   # heinäkuu
    "kesä",   # elokuu
    "syksy",  # syyskuu
    "syksy",  # lokakuu
    "syksy"   # marraskuu
)

kuukausi = int(input("Anna kuukauden numero (1–12): "))

if 1 <= kuukausi <= 12:
    print("Vuodenaika on", vuodenajat[kuukausi - 1])
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

print("Syötetyt nimet:")
for nimi in nimet:
    print(nimi)


lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Lisää uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
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
            print("Lentoasemaa ei löydy.")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta.")
