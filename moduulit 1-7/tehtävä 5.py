leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))
LUOTI_GRAMMOA = 13.3
NAULA_LUOTIA = 32
LEIVISKA_NAULOJA = 20
kokonais_luodit = (
    leiviskat * LEIVISKA_NAULOJA * NAULA_LUOTIA
    + naulat * NAULA_LUOTIA
    + luodit
)
kokonais_grammat = kokonais_luodit * LUOTI_GRAMMOA
kilogrammat = int(kokonais_grammat // 1000)
grammat = kokonais_grammat % 1000
print(f"Massa on {kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")