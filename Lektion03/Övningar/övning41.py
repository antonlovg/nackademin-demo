print("NUMANALYZER")
print("  v1.33.7")

lista = [] # En tom lista som kan fyllas med tal
summa = 0
antal = 0
störst = 0
lägst = 0
medelvärde = float(0)

while True:
    tal = float(input("Ange ett tal: "))
    if tal < 0: # Kollar om talet är negativt, isåfall avbryter vi loopen
        break
    else: # Är talet positivt läggs det in i listan tal
        lista.append(tal) # Lägger till talet i listan

        summa += tal # Lägger till det nya talet till den totala summan
        antal += 1 # Lägger till 1 till antal för att öka hur många tal vi skrivit in
        if tal > störst: # Kollar om värdet tal är större än det som just nu är störst, isåfall hoppar den in i if-satsen och byter ut värdet
            störst = tal
        if tal < lägst: # Kollar om värdet tal är mindre än det som just nu är lägst, isåfall hoppar den in i if-satsen och byter ut värdet
            lägst = tal
        
medelvärde = summa / antal # Räknar ut medelvärde (totala summan dividerat med antal tal)

print(f"Minsta tal: {lägst}\nStörsta tal: {störst}\nSumma: {summa}\nMedelvärde: {medelvärde}")