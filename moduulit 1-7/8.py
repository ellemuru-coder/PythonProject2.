# ------------------------------------------------
# TEHTÄVÄ 8 — LENTOASEMAT + MYSQL + geopy
# ------------------------------------------------

import mysql.connector
from geopy.distance import geodesic


# ------------------------------------------------
# MySQL-yhteys (MUOKKAA OMAT TIEDOT)
# ------------------------------------------------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flight_game"
)


# ------------------------------------------------
# 8A — ICAO → lentokentän nimi ja kunta
# ------------------------------------------------

def hae_lentoasema(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    cursor.close()
    return result


icao = input("Anna ICAO-koodi: ").upper()
tulos = hae_lentoasema(icao)

if tulos:
    print(f"Lentokenttä: {tulos[0]}, {tulos[1]}")
else:
    print("Lentokenttää ei löytynyt.")


# ------------------------------------------------
# 8B — Maakoodi → lentokenttien määrä tyypeittäin
# ------------------------------------------------

def kenttien_lkm_maassa(maakoodi):
    sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
    cursor = connection.cursor()
    cursor.execute(sql, (maakoodi,))
    results = cursor.fetchall()
    cursor.close()
    return results


maakoodi = input("\nAnna maakoodi (esim. FI): ").upper()
data = kenttien_lkm_maassa(maakoodi)

print(f"\nLentokentät maassa {maakoodi}:")
for kenttatyyppi, maara in data:
    print(f"{kenttatyyppi}: {maara} kpl")


# ------------------------------------------------
# 8C — Kahden ICAO-koodin välinen etäisyys
# ------------------------------------------------

def hae_koordinaatit(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    cursor.close()
    return result


icao1 = input("\nAnna ensimmäinen ICAO-koodi: ").upper()
icao2 = input("Anna toinen ICAO-koodi: ").upper()

koord1 = hae_koordinaatit(icao1)
koord2 = hae_koordinaatit(icao2)

if not koord1 or not koord2:
    print("Toinen koodeista ei löytynyt tietokannasta.")
else:
    point1 = (koord1[0], koord1[1])
    point2 = (koord2[0], koord2[1])
    distance_km = geodesic(point1, point2).km
    print(f"\nEtäisyys {icao1} → {icao2}: {distance_km:.2f} km")
