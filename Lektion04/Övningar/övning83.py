todos = ["Städa", "Handla", "Plugga", "Ge blod"]

print(todos)

while True:
    try:
        taBort = int(input("Ta bort i listan (index) > "))
        if 0 <= taBort < len(todos):
            del todos[taBort]
        else:
            print("Fel index, skriv ett tal mellan 0 och", len(todos))
    except ValueError:
        break

    print(todos)

print (todos)
