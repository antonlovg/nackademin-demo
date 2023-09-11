import os

ui_width = 20

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

    print("Lägg till artikel:")
    titel = input(" titel > ")
    text = input(" text > ")
    notes[titel] = text

    for note in notes:
        print("-" * ui_width)
        print("Titel: ", note)
        print("Text: ", notes[note])
    print("-" * ui_width)
    input("Tryck enter för att köra programmet igen...")
    