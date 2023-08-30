# Casting = Typomvandling
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people: "))
answer = myBill / numberOfPeople
answer = round(answer)
print("You all owe", answer)

# Kan även ha round direkt i print
# print("You all owe", round(answer))

# Flytta typomvandling till uträkning.
# myBill = input("What was the bill?: ")
# numberOfPeople = input("How many people: ")
# answer = float(myBill) / int(numberOfPeople)