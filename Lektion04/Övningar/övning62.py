# Övning 6.2

ui_width = 20

print("Robber Translate")
print(ui_width * "-")

konsonant = "bcdfghjklmnpqrstvwxyz"
svenska = input("Svenska \t< ")
rövarspråk = ""

for n in svenska: # Kollar på alla bokstäver i texten man skrivit på svenska
    if n.lower() in konsonant:
        if n.isupper():
            rövarspråk += n + "O" + n
        else:
            rövarspråk += n + "o" + n
    else:
        rövarspråk += n

print("Rövarspråk \t>", rövarspråk)