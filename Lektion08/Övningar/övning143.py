import random


def get_even(nummer):
    jämna_tal = []  # Behöver spara våra jämna tal nånstans
    for n in nummer:
        if n % 2 == 0:
            jämna_tal.append(n)
    return jämna_tal


numbers = []

for x in range(10):
    numbers.append(random.randint(0, 9))

even = get_even(numbers)
print("even", even)
print("numbers", numbers)
