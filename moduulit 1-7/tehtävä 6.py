import random

kolmenumero_koodi = "".join(str(random.randint(0, 9)) for _ in range(3))

nelinumeroinen_koodi = "".join(str(random.randint(1, 6)) for _ in range(4))


print("Kolmenumeroinen koodi (0-9):", kolmenumero_koodi)
print("Nelinumeroinen koodi (1-6):", nelinumeroinen_koodi)