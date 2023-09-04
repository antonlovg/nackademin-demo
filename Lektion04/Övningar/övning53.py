ui_width = 19

print(".: MATHLETE v2.0 :.".center(ui_width))
print(ui_width * "-")
print("> Ange ett tal:")

alla_tal = []
kardinalitet = 0

while True:
    tal = input("> ")
    if tal != "exit":
        try:
            tal = int(tal)
            kardinalitet = kardinalitet + 1
            alla_tal.append(tal)

        except:
            print("FEL: Ogiltigt nummer")
    else:
        break

summa = sum(alla_tal)
medel = summa / kardinalitet

print(ui_width * "-")

print(f"Kardinalitet: \t{kardinalitet}")
print(f"Summa: \t{summa}")
print(f"Medel: \t{medel}")