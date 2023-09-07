todos = ["Städa", "Handla", "Plugga", "Ge blod"]

print(todos)
while True:
    taBort = input(f"Ta bort ett värde från {todos} > ")
    if taBort in todos:
        todos.remove(taBort)
    else:
        print("Felaktig inmatning")
    
    if len(todos) > 0:
        fortsätta = input("Vill du fortsätta ta bort (ja/nej) > ")
        if fortsätta.lower() != "ja":
            break
    else:
        print("Du har inga värden kvar i listan:")
        break
print(todos)