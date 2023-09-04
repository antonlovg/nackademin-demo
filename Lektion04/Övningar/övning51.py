tal = input("tal > ")
try:
    tal = int(tal)
    tal = tal + tal
    print(f"RESULTAT: {tal}")
except:
    print(f"{tal} kan inte översättas till ett heltal")

print("Stänger programmet")