# Order Validation Script
# Unosimo ukupan broj proizvoda;
while True:
    broj_proizvoda = int(input("Unesite broj proizvoda: "))

    if broj_proizvoda < 1 or broj_proizvoda > 50:
        print("Greska: Nevalidan broj proizvoda.")
        continue

# Unosimo cijenu narudzbine;
    cijena = float(input("Unesite cijenu narudzbine: "))

    if cijena <= 0:
        print("Greska: Cijena mora biti veca od 0.")
        continue

# Unosimo status placanja;
    status = input("Unesite status placanja: ")

    print()

    if status == "placeno":
        print("Narudzba moze biti obradjena.")
        break
    elif status == "neplaceno":
        print("Narudzba nije placena, ne moze biti obradjena.")
        break
    elif status == "na cekanju":
        print("Narudzba nije placena, ne moze biti obradjena.")
        break
    else:
        print("Greska: Nepoznat status placanja.")

print()

print(f"Broj proizvoda: {broj_proizvoda}")
print(f"Cijena proizvoda: {cijena}")
print(f"Status placanja: {status}