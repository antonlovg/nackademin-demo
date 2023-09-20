# En klass som beskriver en rektangel

class Rectangle:
    # Attribut
    length = 0
    width = 0

    # Metod
    def area(self):
        return self.length * self.width


# Skapa objekt av klassen
r1 = Rectangle()

# Ändra attribut
r1.length = 5
r1.width = 10


print("Längd:", r1.length)  # 5
print("Bredd:", r1.width)  # 10
print("Area:", r1.area())  # 50

r2 = Rectangle()
r2.width = 10
r2.length = 10
print("Area:", r2.area())
