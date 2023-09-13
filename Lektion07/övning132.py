import requests
import json
import os

ui_width = 20

url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/stockholm"

while True:

    if os.name == "nt":
        os.system("cls")
    
    elif os.name == "posix":
        os.system("clear")

    print("Enter the name of the city\nfor which you want forecasts:")
    stad = input("> ").lower()
    print("-" * ui_width)
    print("FORECASTS".center(ui_width))
    print("*" * ui_width)

    response = requests.get(url, params = {"city":stad}) # Parameter för att ta fram och ersätta integer-delen med Heltatl
    response_dict = json.loads(response.text)

    väder = response_dict["forecasts"]

    for n in väder:
        print(f"{n['date']}\t{n['forecast']}")

    """
    Tidigare lösning innan for-loop
    x0 = väder[0]
    x1 = väder[1]
    x2 = väder[2]
    x3 = väder[3]

    print(f"{x0['date']}\t{x0['forecast']}")
    print(f"{x1['date']}\t{x1['forecast']}")
    print(f"{x2['date']}\t{x2['forecast']}")
    print(f"{x3['date']}\t{x3['forecast']}")
    """

    print("-" * ui_width)
    break

    # forecasts {
    # [0]date : forecast
    # "13 september" : "clear"