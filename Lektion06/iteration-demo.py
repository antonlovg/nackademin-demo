"""

character = {
            'forename':"test", 
            'surename':'orc',
            'occupation':'warrior'
}

for n in character:
    print(character[n])
"""

server = {
    'type': 'firewall',
    'open_ports': [
        1000 ,
        1234 ,
        1337
    ]
}

print(server["open_ports"][0])

