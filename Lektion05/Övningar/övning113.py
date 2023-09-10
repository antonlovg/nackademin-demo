import json
import os

ui_width = 20
nummerserie = []

if os.path.isfile("Lektion05/Övningar/nummerserie.json"):
    try:
        with open("Lektion05/Övningar/nummerserie.json", "r") as f:
            nummerserie = json.load(f)

    except json.JSONDecodeError:
        nummerserie = []
else:
    nummerserie = []

summa = sum(nummerserie)

while True:

    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    print(".:  intMEMORIZER  :.".center(ui_width))
    print("*" * ui_width)
    if not nummerserie:
        print("* Inget heltal angivet ännu")
    for n in nummerserie:
        print("*", n)
    print("-" * ui_width)
    print(f"SUMMA: {summa}")
    print("-" * ui_width)
    print(" \t> mata in heltal")
    print("0\t> stänger script")
    print("rensa\t> rensar listan")
    print("-" * ui_width)

    val = input("> ")
    if val == "rensa":
            riktigt_val = input("Säker på att du vill rensa listan? (j/n) > ").lower()
            if riktigt_val == "j":
                nummerserie.clear()
                summa = sum(nummerserie)
                with open("Lektion05/Övningar/nummerserie.json", "w+") as f:
                    json.dump(nummerserie, f)

                input("Listan rensad, tryck enter för att fortsätta...")

            elif riktigt_val == "n":
                input("Listan är inte rensad, tryck enter för att fortsätta...")

            else:
                input("Ange j (= ja) eller n (= nej), tryck enter för att försöka igen...")
    else:
        try:
            val_nummer = int(val)
            if int(val_nummer) != 0 and val_nummer not in nummerserie:
                nummerserie.append(val_nummer)
                summa = sum(nummerserie)

                with open("Lektion05/Övningar/nummerserie.json", "w+") as f:
                    json.dump(nummerserie, f)

            elif int(val_nummer) == 0:

                if os.name == "nt":
                    os.system("cls")
    
                elif os.name == "posix":
                    os.system("clear")
                
                with open("Lektion05/Övningar/nummerserie.json") as f:
                    resultat = f.read()

                print("Programmet stängdes!\n\nStrax innan programmet stängdes\nså skreves följande sträng till\ntextfilen nummerserie.json:")
                print(f"\n\"{resultat}\"".center(ui_width))
                print("\nNästa gång du kör programmet\nkommer nummerserie.json läsas\nin på nytt.")
                input("Tryck enter för att köra igen...")

            elif int(val_nummer) in nummerserie:
                input("Heltal finns redan i listan, tryck enter för att försöka igen...")
            else:
                input("Ange ett heltal, tryck enter för att försöka igen...")
        except ValueError:
            input("Ange ett heltal, tryck enter för att försöka igen...")
