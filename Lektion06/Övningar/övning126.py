import os
import json

ui_width = 20

notes = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg!": "Ta bilen till verkstad",
    "Inför tentamen" : "Gör alla instuderingsuppgifter"
}

if os.path.isfile("Lektion06/Övningar/notes.json"):
    try:
        with open("Lektion06/Övningar/notes.json", "r") as f:
            notes = json.load(f)

    except json.JSONDecodeError:
        notes = {
            "Meddelande från skolan": "Friluftsdag på tisdag",
            "Kom ihåg!": "Ta bilen till verkstad",
            "Inför tentamen" : "Gör alla instuderingsuppgifter"
        }
    

while True:

    with open("Lektion06/Övningar/notes.json", "w+") as f:
        json.dump(notes, f)

    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    print(".:  ALWAYSNOTE  :.".center(ui_width))
    print(".  gold edition  -".center(ui_width))
    print("*" * ui_width)
    
    if not notes:
        print("Här var det tomt!")

    for note in notes:
        print("-", note)
        #print("Text: ", notes[note])

    print("-" * ui_width)
    print("view\t| view note")
    print("add\t| add note")
    print("rm\t| remove note")
    print("exit\t| exit")
    print("-" * ui_width)
    
    val = input("menu > ")
    print("-" * ui_width)

    if val == "view":
        view_note = input("title > ")
        try:
            print("-" * ui_width)
            print(notes[view_note])
            input("Tryck på enter för att fortsätta...")
        except KeyError:
            print("-" * ui_width)
            input("FEL: Du angav ett värde som inte finns")
    
    elif val == "add":
        add_title = input("title > ")
        add_descr = input("descr > ")
        notes[add_title] = add_descr
        print("-" * ui_width)
        print("INFO: Note added")
        print("-" * ui_width)
        input("Tryck på enter för att fortsätta...")
    
    elif val == "rm":
        ta_bort = input("title > ")
        del notes[ta_bort]
        print("-" * ui_width)
        print("INFO: Note deleted")
        print("-" * ui_width)
        input("Tryck på enter för att fortsätta...")
    
    elif val == "exit": # Gör en exit-window
        break
    
    else:
        print(f"FEL: Du angav felaktigt val ({val})")
        print("-" * ui_width)
        input("Tryck på enter för att fortsätta...")
