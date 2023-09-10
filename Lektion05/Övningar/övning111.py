import json

random_stuff = [1337, 13.37, "Ååh Yää!"]

with open("Lektion05/Övningar/data_random_stuff.json", "w+") as f:
    f.write(json.dumps(random_stuff))
    f.seek(0)
    läsa = f.read()

# Alternativ lösning istället för w+ och seek:
#with open("Lektion05/Övningar/data_random_stuff.json") as f:
    #läsa = f.read()

print(läsa)