person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris","age": 3,"type": "hund"},
        {"name": "Lisa","age": 2,"type": "katt"},
        {"name": "Lassie","age":1,"type":"häst"}
    ]
}


# MED VARIABLER
namn = person["firstname"] + " " + person["lastname"]
age = person["age"]
pets = person["pets"]
pets_count = len(pets)

print("... ÖVNING ...")
print(f"{namn} är {age} år gammal och har {pets_count} husdjur: ")
for pet in pets:
    print(f"* En {pet['age']} år gammal {pet['type']} som heter {pet['name']}")


#print(person["firstname"], person["lastname"], "är", [person["age"]], "år gammal och har", len(person["pets"]), "husdjur:")
#for n in person:
    #print("* En", pet_age)