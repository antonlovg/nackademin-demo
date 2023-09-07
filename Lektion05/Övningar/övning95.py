import os

ui_width = 30

bilar = ["Mercedes", "Volvo", "Toyota"]

while True :
    
    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    print(".:  STACKMASTER v1.33.7  :.".center(ui_width))
    print("-" * ui_width)
    if not bilar:
        print(":(".center(ui_width))
        print("* EMPTY *".center(ui_width))
    for bil in bilar:
        print("- " + bil)
    
    print("-" * ui_width)
    print("| MENU |".center(ui_width))
    print("-" * ui_width)
    print("push |\tPush element to stack")
    print("pull |\tPull element from stack")
    print("exit |\tExit program")
    print("-" * ui_width)
    val = input("MENU > ")
    if val == "push":
        item = input("ITEM > ")
        bilar.append(item)
    elif val == "pull":
        bilar.pop()
    elif val == "exit":
        break
    else:
        input("ERROR: Unknown command\nPress enter to continue...")
