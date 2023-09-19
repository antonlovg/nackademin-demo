# Göra om miles till km och vice versa

dist = input("Ange distans > ").lower()


def km_to_miles(dist_km):
    omvandla = dist_km * 0.621371
    return omvandla


def miles_to_km(dist_miles):
    omvandla = dist_miles * 1.60934
    return omvandla


dist = dist.strip()  # Ta bort allt onödigt i användarens inmatning ->
# https://www.w3schools.com/python/ref_string_strip.asp

if dist.endswith("km"):
    dist = dist.replace("km", "")
    try:
        # dist = float(dist)
        omvandlad_dist = km_to_miles(float(dist))
        print(f"{dist}km motsvarar {omvandlad_dist} miles.")
    except ValueError:
        print("Ange ett nummer följt av km")

elif dist.endswith("miles"):
    dist = dist.replace("miles", "")
    try:
        omvandlad_dist = miles_to_km(float(dist))
        print(f"{dist}miles motsvarar {omvandlad_dist} km.")
    except ValueError:
        print("Ange ett nummer följt av miles")
else:
    print("Ange ett nummer följt av km eller miles")
