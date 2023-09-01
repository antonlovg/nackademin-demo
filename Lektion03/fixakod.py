# Övning - Fixa if-loop
order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese? ")
  if cheese == "yes":
    print("You got it.")
  else:
    print("No cheese it is.")
if order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that? ")
  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")

# Övning - Fixa while-loop
'''
while True:
  color = input("Enter a color: ")
  if color == "red":
#    print("Cool color!")
     break
  else:
    print("Cool color!")
    print("I don't like red")
'''

# Exempel continue/exit
'''
while True:
  print("You are in a corridor, do you go left or right? ")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")
'''

# Exempel for-loop
'''
total = 0
for counter in range(100):
  total += 10
  print(total)
'''

# Övning
'''
print("Ange ett startnummer:")
startNummer = input("> ")
print("Ange ett slutnummer:")
slutNummer = input("> ")
print("Ange hur snabbt nummer ska ökas:")
incrementNummer = input("> ")
'''
