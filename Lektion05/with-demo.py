attendants = ['Lisa', 'Kalle', 'Olivia', 'Johan']

with open('textfil.txt', 'w') as minFil:
    for attendant in attendants:
        minFil.write('Hello ' + attendant + '!\n')