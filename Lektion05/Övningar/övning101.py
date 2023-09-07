import os

ui_width = 30

if os.path.isfile("sign.txt"):
    with open("sign.txt", "r") as f:
        meddelande = f.read()
else:
    meddelande = "Inget hinder på vägen"


while True:
    
    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    
        
    print("-" * ui_width)
    print(".:  VÄGMEDDELANDE  :.".center(ui_width))
    print("-" * ui_width)
    print("|", meddelande.center(ui_width), "|")
    print("-" * ui_width)
    print("C |\tChange sign message")
    print("E |\tExit program")
    print("-" * ui_width)

    val = input("val > ").lower()

    if val == "c":
            meddelande = input("meddelande > ")
            with open("sign.txt", "w") as f:
                f.write(meddelande)
    elif val == "e":
        break
    else:
        input("ERROR: Unknown command\nPress enter to continue...")