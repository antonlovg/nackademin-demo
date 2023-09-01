import random

print(".:THE HIGHER LOWER GAME:.")
print("-------------------------")
print("Welcome to the Higher Lower\nGame. I will randomise a\nnumber between 0 and 99.")
print("Can you guess it?")
print("-------------------------")
guess = int(input("Your guess > "))
tal = random.randint(0, 99)
räknare = 0

while True:
    if guess == tal:
        print("-------------------------")
        print(f"{guess} is correct!")
        print(f"It took you {räknare} guesses")
        print("Good job!")
        break
    elif guess >= tal:
        print("LOWER")
        guess = int(input("TRY AGAIN > "))
        räknare += 1
    elif guess <= tal:
        print("HIGHER")
        guess = int(input("TRY AGAIN > "))
        räknare += 1