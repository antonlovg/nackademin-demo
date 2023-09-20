import random

numbers = []

for x in range(10):
    numbers.append(random.randint(0,20))

numbers_sorted = sorted(numbers)

print("BEFORE SORTING:")

for n in numbers:
    print("-", n)

print("AFTER SORTING:")

for n in numbers_sorted:
    print("-", n)
