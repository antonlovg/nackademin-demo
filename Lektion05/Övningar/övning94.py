ui_width = 20

todos = ["Städa", "Handla", "Plugga", "Ge blod"]

print(".:    TODOIFY    :.".center(ui_width))
print(ui_width * "*")


for todo in todos:
    print("- " + todo)