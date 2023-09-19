# Göra om miles till km och vice versa

dist = input("Ange distans > ").lower()

def km_to_miles(dist_km):
    omvandla = dist / 0,621371
    return omvandla
    
def miles_to_km(dist_miles):
    omvandla = dist * 1,60934
    return omvandla

if dist.endswith == "km":
    omvandlad_dist = km_to_miles()
    print(f"{dist} motsvarar {omvandlad_dist} miles.")
else:
    omvandlad_dist = miles_to_km()
    print(f"{dist} motsvarar {omvandlad_dist} km.")