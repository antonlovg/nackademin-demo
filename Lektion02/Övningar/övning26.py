vanlig2 = int(input("Hur många vill äta 2 vanliga korvar? "))
vanlig3 = int(input("Hur många vill äta 3 vanliga korvar? "))
vegansk2 = int(input("Hur många vill äta 2 veganska korvar? "))
vegansk3 = int(input("Hur många vill äta 3 veganska korvar? "))

dryck = vanlig2+vanlig3+vegansk2+vegansk3
vanlig = (vanlig2*2)+(vanlig3*3)
vegansk = (vegansk2*2)+(vegansk3*3)

vanligpkt = (vanlig//8) # Antal paket som behöver köpas när det är 8 korvar per förpackning
vanligpkt_decimal = (vanlig%8)
if vanligpkt_decimal > 0: # Lägger till värde 1 till vanligtpkt då heltalsdivision annars avrunder nedåt, för att få rätt antal paket
    vanligpkt+=1
veganskpkt = (vegansk//4) # Likadant som ovan fast för veganska korvar och det är 4 per förpackning
veganskpkt_decimal = (vegansk%8)
if veganskpkt_decimal > 0: # Lägger till värde 1 till veganskpkt då heltalsdivision annars avrundar nedåt, för att få rätt antal paket
    veganskpkt+=1

kostnad = round((vanligpkt*20.95)+(veganskpkt*34.95)+(dryck*13.95), 2) # Uträkning av totala kostnaden

print(".: KORVKOLLEN 1.0.1 :.")
print("----------------------")
print("Hur många elever vill ha...")
print("2 vanliga korvar: ", vanlig2)
print("3 vanliga korvar: ", vanlig3)
print("2 veganska korvar: ", vegansk2)
print("3 veganska korvar: ", vegansk3)
print("----------------------")
print("-     INKÖPSLISTA    -")
print("----------------------")
print("| Vanlig korv: ", vanligpkt, "förpackningar")
print("| Vegansk korv: ", veganskpkt, "förpackningar")
print("| Dryck: ", dryck, "drickor")
print("----------------------")
print("| ", kostnad, "SEK")
print("----------------------")
print("Det totala priset blir: ", kostnad)