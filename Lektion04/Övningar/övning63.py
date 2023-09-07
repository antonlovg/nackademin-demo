# Övning 6.3

# if mening == mening[::-1] = tar alla tecken i strängen i omvänd ordning

skrivMening = input("Ange en mening > ")

palindrom = skrivMening.replace(" ", "").lower() # Vi bryr oss inte om HUR användaren skrivit in, så istället för mellanslag så är det tomt och alla tecken konverteras till små med lower()

if palindrom == palindrom[::-1]: # Slicing-metod
    print(f"{skrivMening} är ett palindrom.")
else:
    print(f"{skrivMening} är inget palindrom.")