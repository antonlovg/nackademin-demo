# Övning 6.1
"""
ange_text = [input("Ange en text: ")]
text_längd = len(ange_text)
ange_bokstav = input("Ange en bokstav: ")

print(len(ange_text))

"""

print("Ange en text")
angeText = input("> ")

print("Ange bokstav")

while True:
    angeBokstav = input("> ").lower()
    if angeBokstav.isalpha():
        break
    else:
        print("Du angav inte en bokstav, testa igen")

förekomst = 0
n = 0

while n < len(angeText):
    if angeText[n].lower() == angeBokstav:
        förekomst += 1
    n += 1

print(f"Bokstaven {angeBokstav} förekommer {förekomst} gånger i texten.")

