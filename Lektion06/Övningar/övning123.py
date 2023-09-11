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

    for note in notes:
        print("-" * ui_width)
        print("Titel: ", note)
        print("Text: ", notes[note])
    print("-" * ui_width)
    break