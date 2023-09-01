tal1 = int(input("Ange ett tal: "))
tal2 = int(input("Ange ett till tal: "))
tal3 = int(input("Ange ett sista tal: "))
print("---------")
if tal1 >= tal2 and tal1 >= tal3:
    print("Det största talet är: ", tal1)
elif tal2 >= tal1 and tal2 >= tal3:
    print("Det största talet är: ", tal2)
else:
    print("Det största talet är: ", tal3)