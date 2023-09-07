# Ange bredden på gränssnittet
ui_width = 20

# Skapa en dictionary för att hålla reda på förekomsten av varje siffra (0-9)
förekomst = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

# Öppna filen "numbers.csv" och läs innehållet
with open("Lektion05/Övningar/numbers.csv") as f:
    nummer = f.read()

# Utskrift av programmets titel och separatorer
print("-" * ui_width)
print("- NUMANALYZER - ".center(ui_width))
print("-" * ui_width)

# Loopa genom varje tecken i inlästa numret
for n in nummer:
    # Kontrollera om tecknet är en siffra (0-9)
    if n.isdigit():
        # Konvertera tecknet till ett heltal och öka förekomsten i dictionary
        siffra = int(n)
        förekomst[siffra] += 1

# Loopa igenom dictionary för att skriva ut resultatet
for siffra, antal in förekomst.items():
    # Skriv ut siffran och dess förekomst, separerat av ett tab-tecken
    print(f"| {siffra} |\t{antal}")

# Utskrift av separatorer
print("-" * ui_width)
