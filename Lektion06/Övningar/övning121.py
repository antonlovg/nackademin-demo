import os

ui_width = 10

notes = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg!": "Ta bilen till verkstad",
    "Inför tentamen" : "Gör alla instuderingsuppgifter"
}

while True:

    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    choice = input("Anteckning > ")
    print("-" * ui_width)
    try:
        print(notes[choice])
        print("-" * ui_width)
        input("Tryck enter för att försöka igen...")
    except KeyError:
        input("FEL: Anteckning finns inte...")