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

    print(".: ANTECKNINGAR :.".center(ui_width))
    print("*" * ui_width)
    for note in notes:
        print("-", note)
    print("-" * ui_width)
    break