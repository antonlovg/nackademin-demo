ui_width = 20

# Ritar intro
print(ui_width * '*')
print("*", 'The Great Divider'.center(ui_width), "*") # Kolla varför det blir mellanrum
print(ui_width * '-')
print("")
print('Beräknar c för uttrycket:'.center(ui_width))
print('a / b = c'.center(ui_width))
print("")
print(ui_width * "-")

while True:
    tal_a = input("Ange tal a > ")
    try:
        tal_a = float(tal_a)
        break
    except:
        print("FEL: Ogiltigt nummer")

while True:
    tal_b = input("Ange tal b > ")
    try:
        tal_b = float(tal_b)
        break
    except:
        print("FEL: Ogiltigt nummer")

print(ui_width * "-")

try:
    tal_b != 0
    tal_c = tal_a / tal_b
    print(tal_c)
except:
    print("FEL: Division med 0")