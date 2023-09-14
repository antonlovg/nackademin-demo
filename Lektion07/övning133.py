import json
import os
import requests

ui_width = 20

url_artister = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

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

    val = input("> ").lower()
    print("-" * ui_width)

    response = requests.get(url_artister, params = {'name':val}) # Parameter för att ta fram och ersätta integer-delen med Heltatl
    response_dict = json.loads(response.text)

    artist_lista = response_dict['artists']
    
    # Se if-sats, där vi använder None
    artist_id = None

    # Precis som i uppgift 13.2 samt som Mahmuds genomgång av "pets" (iteration-demo)
    for n in artist_lista:
        if n['name'].lower() == val:
            artist_id = n['id']
            break
    
    # https://www.w3schools.com/python/ref_keyword_none.asp för att kolla så variable artist_id inte är tom (hade inte for-loopen hittat nåt hade artist_id varit tom)
    if artist_id is not None:

        # Lägger ihop urlerna (dvs sista siffrorna som är id vi tog fram läggs in i slutet av url)
        url_id = url_artister + artist_id
        
        #
        response = requests.get(url_id)
        response_dict = json.loads(response.text)

        # Testar alla variablar
        artist = response_dict['artist']
        artist_genre = artist['genres'] # Smma sak som response_dict['artist']['genres']
        artist_active = artist['years_active'] # Samma sak som response_dict['artist']['years_active']
        artist_members = artist['members'] # Samma sak som response_dict['artist']['members']
        artist_name = artist['name'] # Samma sak som response_dict['artist']['name']

        print(f"Genre: {artist_genre}")
        print(f"Active: {artist_active}")
        print(f"Members: {artist_members}")
        print(f"Name: {artist_name}")

        print("Genres:")
        for genres in artist_genre:
            print(f"{genres}", end = "")
        print(f"")

        # print(response_dict)
        input("...")

    else:
        input(f"{val} fanns inte i listan, tryck enter för att försöka igen...")














    #for n in artist_namn:
        # Tar bara fram id om vi hittar namnet som användaren angett
        #if n['name'].lower() == val: # Letar efter namnet vi skriver tidigare i val::
            #artist_id = n['id']
            #print(f"{artist_id}")

# url_artister = artists [{name:id}]


