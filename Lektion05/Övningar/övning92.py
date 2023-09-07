registrerade = ["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmalningar = ["Anna", "Erik", "Karl"]

for n in avanmalningar:
    if n in registrerade:
        registrerade.remove(n)

print(registrerade)
