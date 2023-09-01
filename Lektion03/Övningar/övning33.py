import random

dice = random.randint(1, 6)

if dice == 1:
    print(f"Du slog siffra {dice}")
    print("-----\n|   |\n| o |\n|   |\n-----")
elif dice == 2:
    print(f"Du slog siffra {dice}")
    print("-----\n|o  |\n|   |\n|  o|\n-----")
elif dice == 3:
    print(f"Du slog siffra {dice}")
    print("-----\n|o  |\n| o |\n|  o|\n-----")
elif dice == 4:
    print(f"Du slog siffra {dice}")
    print("-----\n|o o|\n|   |\n|o o|\n-----")
elif dice == 5:
    print(f"Du slog siffra {dice}")
    print("-----\n|o o|\n| o |\n|o o|\n-----")
else:
    print(f"Du slog siffra {dice}")
    print("-----\n|o o|\n|o o|\n|o o|\n-----")