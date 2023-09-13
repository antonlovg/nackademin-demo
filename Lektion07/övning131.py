import requests
import json

url = "https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=100"

heltal = input("Ange heltal: ")

response = requests.get(url, params = {"integer":heltal}) # Parameter för att ta fram och ersätta integer-delen med Heltatl
response_dict = json.loads(response.text)

factors = response_dict['factors']
even = response_dict['even']
prime = response_dict['prime']

if even == False:
    if prime == False:
        print(f"{heltal} är ett ojämnt nummer. Numret är inte ett primtal.\nNumrets faktorer är {factors}")
    else:
        print(f"{heltal} är ett ojämnt nummer. Numret är ett primtal.\nNumrets faktorer är {factors}")
else:
    if prime == True:
        print(f"{heltal} är ett jämnt nummer. Numret är ett primtal.\nNumrets faktorer är {factors}")
    else:
        print(f"{heltal} är ett jämnt nummer. Numret är inte ett primtal.\nNumrets faktorer är {factors}")