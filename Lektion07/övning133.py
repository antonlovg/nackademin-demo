import json
import os
import requests

ui_width = 20

url_artister = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'
unik_id = ''
url_id = url_artister + unik_id

while True:

    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    print("----- ARTIST DB -----".center(ui_width))
    print("Ariana Grande")
    print("Avicii")
    print("Blink-182")
    print("Brad Paisley")
    print("Ed Sheeran")
    print("Imagine Dragons")
    print("Maroon 5")
    print("Scorpions")
    print("-" * ui_width)
    print("Select artist:")

    val = input("> ")
    print("-" * ui_width)

    response = requests.get(url_artister, params = {'name':val}) # Parameter för att ta fram och ersätta integer-delen med Heltatl
    response_dict = json.loads(response.text)

    artist_namn = response_dict['artists'][0]
    print(artist_namn)
    break

# url_artister = artists [{name:id}]


