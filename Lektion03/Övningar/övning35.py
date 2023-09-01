kön = input("Ange ditt kön (man/kvinna): ")
while True:
   if kön == "man" or kön == "kvinna":
       break
   else:
       kön = input("Ange ditt kön i rätt format (man/kvinna): ")

hårfärg = input("Ange din hårfärg: ")

ögonfärg = input("Ange din ögonfärg: ")

print("-------")

if kön == "kvinna" and hårfärg == "brun" and ögonfärg == "brun":
    print("Du matchar med Emma Watson och Selena Gomez")
elif kön == "man" and hårfärg == "röd" and ögonfärg == "blå":
    print("Du matchar med Rupert Grint")
elif kön == "man" and hårfärg == "brun" and ögonfärg == "brun":
    print("Du matchar med Daniel Radcliffe och Anton Lövgren")
elif kön == "man" and hårfärg == "brun" and ögonfärg == "grön":
    print("Du matchar med Anders Andersson och Andreas Andreasson")
elif kön == "man" and hårfärg == "brun" and ögonfärg == "grön":
    print("Du matchar med Leif GW Persson och Göran Persson")
else:
    print("Du matchar inte med någon")