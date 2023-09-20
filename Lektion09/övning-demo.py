from random import randint


class Rectangle:
    def __init__(self, length, height):
        # Privata attribut
        self.__length = length
        self.__height = height

    # Getters & Setters
    def get_length(self):
        return self.__length

    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            print("| Fel värde i length")

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("| Fel värde i height")

    # Metoder
    def rectangle_omkrets(self):
        omkrets = (self.get_length() + self.get_height()) * 2
        return omkrets

    def area(self):
        return self.get_length() * self.get_height()


# Skapar objekt av klassen
r1 = Rectangle(10, 15)
print("| Rectangle r1")
print("| Omkrets:", r1.rectangle_omkrets())
print("| Height:", r1.get_height())
print("| Length:", r1.get_length())
print("-" * 15)

r2 = Rectangle(30, 5)
print("| Rectangle r2")
print("| Area:", r2.area())
print("| Height:", r2.get_height())
print("| Length:", r2.get_length())
print("-" * 15)

r3 = Rectangle(3, 3)
print("| Rectangle r3")
r3.set_height(10)
r3.set_length(-30)
print("| Area:", r3.area())
print("| Omkrets:", r3.rectangle_omkrets())
print("-" * 15)

r_lista = [
    Rectangle(1, 2),
    Rectangle(3, 4),
    Rectangle(5, 6)
]

print("| Area i en lista")


def get_area_summa(r_lista):
    summa = 0
    for r in r_lista:
        summa += r.area()
        # print("|", r.area())
    return summa


print("| Summa av alla areor", get_area_summa(r_lista))
# print("| Summa av alla areor:", summa)


print("-" * 15)

slump_lista = []
for n in range(1000):
    slump_lista.append(Rectangle(randint(1, 100), randint(1, 100)))

print("| Summa av slumpmässiga areor:", get_area_summa(slump_lista))
