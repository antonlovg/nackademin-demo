import json
import os
import requests

ui_width = 20

# API
url_artister = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

while True:

    # Clearar terminalen
    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    # Skapar mitt UI
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

    response = requests.get(url_artister, params = {'name':val}) # Parameter för att ta fram och ersätta integer-delen med val
    response_dict = json.loads(response.text)

    artist_lista = response_dict['artists']
    
    # Se if-sats, där vi använder None
    artist_id = None

    # Precis som i uppgift 13.2 samt som Mahmuds genomgång av "pets" (iteration-demo) för att ta fram id och anger det till artist_id
    for n in artist_lista:
        if n['name'].lower() == val:
            artist_id = n['id']
            break
    
    # https://www.w3schools.com/python/ref_keyword_none.asp för att kolla så variable artist_id har ett värde (hade inte for-loopen hittat nåt hade artist_id varit None fortfarande)
    if artist_id is not None:

        # Lägger ihop urlerna (dvs sista siffrorna som är id vi tog fram läggs in i slutet av url)
        url_id = url_artister + artist_id
        
        # Hämtar den nya informationen vi har nu med den nya apin
        response = requests.get(url_id)
        response_dict = json.loads(response.text)

        #for genres in artist_genre:
        print(response_dict['artist']['name'])
        print("*" * ui_width)
        print(f"Genres: {', '.join(response_dict['artist']['genres'])}") # https://www.w3schools.com/python/ref_string_join.asp Använder denna method för att printa ut allt på samma rad
        print(f"Years active: {', '.join(response_dict['artist']['years_active'])}")
        print(f"Members: {', '.join(response_dict['artist']['members'])}")
        print("-" * ui_width)

        # print(response_dict)
        input("Tryck enter för att gå tillbaka till menyn...")

    else:
        input(f"{val} fanns inte i listan, tryck enter för att försöka igen...")







         # Hade denna i if-satsen, efter response_dict
        # Testar alla variablar
        #artist = response_dict['artist']
        #artist_genre = artist['genres'] # Smma sak som response_dict['artist']['genres']
        #artist_active = artist['years_active'] # Samma sak som response_dict['artist']['years_active']
        #artist_members = artist['members'] # Samma sak som response_dict['artist']['members']
        #artist_name = artist['name'] # Samma sak som response_dict['artist']['name']

        #print(f"Genre: {artist_genre}")
        #print(f"Active: {artist_active}")
        #print(f"Members: {artist_members}")
        #print(f"Name: {artist_name}")






    #for n in artist_namn:
        # Tar bara fram id om vi hittar namnet som användaren angett
        #if n['name'].lower() == val: # Letar efter namnet vi skriver tidigare i val::
            #artist_id = n['id']
            #print(f"{artist_id}")

# url_artister = artists [{name:id}]


