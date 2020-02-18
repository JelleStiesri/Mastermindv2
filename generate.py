import random
"""Deze functie maakt alle mogelijke combinaties"""
def gen(): # Maakt een lijst met alle mogelijke combinaties van de cijfers 1/6 en met 4 tekens te gelijk
    lijst = []
    fout = 0
    while True:
        combinatie = []
        for getal in range(4):
            los_getal = random.randrange(1, 7)
            combinatie.append(los_getal)
        if combinatie in lijst:
            fout = fout + 1
            continue
        else:
            lijst.append(combinatie)
        if len(lijst) == 1296: #aantal mogelijke combinaties
            break
    lijst.sort(key=lambda x: x[0]) #sorteert alleen op eerste karakter in lijst, verder is niet nodig
    return(lijst)

