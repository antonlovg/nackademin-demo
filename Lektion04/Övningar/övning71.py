import os

ui = 20

POST_1 = ""
POST_2 = ""
POST_3 = ""


while True :
    
    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    print ( ".: basicBILLBOARD :.".center(ui))
    print (ui * "*")
    print ( "P1 > " , POST_1)
    print ( "P2 > " , POST_2)
    print ( "P3 > " , POST_3)
    print (ui * "-")
    print ( "c | Ändra post")
    print ( "e | Stäng program")
    print (ui * "-")
    meny = input("meny > ")
    
    if meny == "c":
        val = input("id > ")
        if val == "1":
            POST_1 = input("meddelande > ")
        elif val == "2":
            POST_2 = input("meddelande > ")
        elif val == "3":
            POST_3 = input("meddelande > ")
        else:
            print("- FEL: Felaktigt ID")
            print("- INFO: Vänligen ge heltal mellan 1-3")
            print(ui * "-")
    
    elif meny == "e":
        exit()
    
    else:
        print(f"- FEL: Okänt kommando ({meny})")
        print(ui * "-")

    input ( "Tryck enter för att fortsätta...")