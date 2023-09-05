todos = ["Städa", "Handla", "Plugga", "Ge blod"]

print(todos)

while True:
    angeTodo = input("Ange todo > ")
    
    if angeTodo in todos:
        print(f"{angeTodo} finns i listan!")
    
    else:
        svar = input(f"{angeTodo} finns inte i listan, vill du lägga till den (J/N)? > ")
        
        if svar.lower() == "j":
            todos.append(angeTodo)
            print(f"{angeTodo} tillagd!")
        
        else:
            print(todos)

    if len(todos) > 0:
        fortsätta = input("Vill du fortsätta (ja/nej) > ")

    if fortsätta.lower() != "ja":
        break

print(todos)