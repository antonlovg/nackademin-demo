land = input("Vänligen ange ett land för att se om det tillhör Norden eller Storbritannien: ").lower()

if land == "danmark" or "finland" or "island" or "norge" or "sverige":
    print("Detta land tillhör Norden.")
    exit()
elif land == "england" or "nordirland" or "skottland" or "wales":
    print("Detta land tillhör Storbritannien.")
    exit()
print("Detta land tillhör varken Storbritannien eller Norden.")