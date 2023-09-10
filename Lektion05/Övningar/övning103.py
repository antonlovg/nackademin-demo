import os
import csv

ui_width = 20

#ID[0],FORENAME[1],SURNAME[2],GENDER[3],YEAR[4]

with open("Lektion05/Övningar/database.csv") as csvfile: # Öppnar CSV-fil och gör person till en list, se https://www.w3schools.io/file/python-csv-read-write/
    csv_reader = csv.reader(csvfile)
    person = list(csv_reader)

while True: # Hela koden

    # Rensar terminalen efter varje användning för att göra det snyggare
    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    # Utskrift av programmets namn samt de olika val som går att görea
    print("-" * ui_width)
    print("- PEOPLES DATABASE - ".center(ui_width))
    print("-" * ui_width)
    print("get_id\t| Get person by ID")
    print("scan_f\t| List people by FORENAME")
    print("scan_s\t| List people by SURNAME")
    print("scan_g\t| List people by GENDER")
    print("scan_y\t| List people by YEAR")
    print("exit\t| Exit program")
    print("-" * ui_width)

    # LÅter användaren göra ett val
    val = input("| > ").lower()
    print("-" * ui_width)
    # ID-val
    if val == "get_id":
        id = input("| ID = ")
        if id.isdigit(): # Kollar så det är en siffra, annars hoppar den över allt
            found = False 
            for row in person: # For loop för att kolla igenom rader
                if row[0] == id: # ID ligger på första raden (index 0)
                    found = True
                    print("-" * ui_width)
                    print(f"| ID:\t\t{row[0]}")
                    print(f"| FORENAME:\t{row[1]}")
                    print(f"| SURNAME:\t{row[2]}")
                    print(f"| GENDER:\t{row[3]}")
                    print(f"| YEAR:\t\t{row[4]}")
                    print("-" * ui_width)
                    input("| Press enter to continue...")
                    break
            if not found:
                input("| Finns ingen person med det ID:t")
                break    
        else: 
            print("-" * ui_width)
            input("| ID behöver vara en siffra, försök igen...")
    # Forename-val
    elif val == "scan_f":
        forename = input("| FORENAME = ").lower()
        if forename.isalpha(): # Kollar så det är bokstäver
            found = False
            for row in person:
                if row[1].lower() == forename:
                    found = True
                    # Skriver allt på en rad då det är många alternativ som ska tas fram
                    print(f"| {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")
            if found:
                print("-" * ui_width)
                input(f"| Alla personer med FORENAME {forename} har hittats, tryck enter för att fortsätta...")
            else:
                print("-" * ui_width)
                input(f"| Hittade ingen med FORENAME {forename}, tryck enter för att fortsätta...")
        else:
            print("-" * ui_width)
            input("| FORENAME får bara innehålla bokstäver, försök igen...")
    # Surname-val
    elif val == "scan_s":
        surname = input("| SURNAME = ")
        if surname.isalpha():
            found = False
            for row in person:
                if row[2] == surname:
                    found = True
                    print(f"| {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")
            if found:
                print("-" * ui_width)
                input(f"| Alla personer med SURNAME {surname} har hittats, tryck enter för att fortsätta...")
            else:
                print("-" * ui_width)
                input(f"| Hittade ingen med SURNAME {surname}, tryck enter för att fortsätta...")
        else:
            print("-" * ui_width)
            input("| SURNAME får bara innehålla bokstäver, försök igen...")
    # Gender-val
    elif val == "scan_g":
        gender = input("| GENDER (Male/Female) = ").lower()
        if gender == "male" or gender == "female":
            found = False
            for row in person:
                if row[3] == gender:
                    found = True
                    print(f"| {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")
            if found:
                print("-" * ui_width)
                input(f"| Alla personer med GENDER {gender} har hittats, tryck enter för att fortsätta...")
            else:
                print("-" * ui_width)
                input(f"| Hittade ingen med GENDER {gender}, tryck enter för att fortsätta...")
        else:
            print("-" * ui_width)
            input("| GENDER måste vara antingen male eller female (ej skifteskänslig), tryck enter för att fortsätta...")
    # Year-val
    elif val == "scan_y":
        year = input("| YEAR = ")
        if year.isdigit():
            found = False
            for row in person:
                if row[4] == year:
                    found = True
                    print(f"| {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")
            if found:
                print("-" * ui_width)
                input(f"| Alla personer med YEAR {year} har hittats, tryck enter för att fortsätta...")
            else:
                print("-" * ui_width)
                input(f"| Hittade ingen med YEAR {year}, tryck enter för att fortsätta...")
        else:
            print("-" * ui_width)
            input("| YEAR får bara innehålla siffrior, försök igen...")
    # STänger programmet
    elif val == "exit":
        break
    # Man har skrivit ett val som inte finns
    else:
        input("| ERROR: Ange ett korrekt val...")