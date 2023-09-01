nummer = int(input("Ange multiplikationstabell> "))
tabell = 1 # Börjar 
for n in range(tabell, tabell + 3): # Inom vilken range som det ska Start, Stop. I detta fall 1 då tabell börjar med 1, och vi vill stoppa efter 3 gånger
    resultat = nummer * n # Resultatet tar det nummer vi har angett * n (i detta fall 1, 2, 3)
    print(resultat) # Skriver ut resultat
    tabell += 1 # Ökar tabells värde med 1 varje gång for-loopen körs 

while True:
    fortsätta = input("Vill du lägga in ytterligare tre tal från tabellen (ja/nej)? ").lower() # Frågar om användaren vill fortsätta lägga in tal.
    if fortsätta == "ja":
        for n in range (tabell, tabell + 3):
            tabell += 1 # Ökar tabells värde med 1 varje gång for-loop
            resultat = nummer * n # Multiplicerar nummer (i detta fall med 4, 5, 6)
            print(resultat) # Skriver ut resultatet
    elif fortsätta == "nej":
        print("Programmet stängs av.")
        break
    else:
        print("Du behöver svara med ja eller nej")