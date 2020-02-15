import random
from Raad_algoritme import algoritme

def menu():
    antwoord = []
    print("welke spelmodus wil je spelen",'\n',"1: Speler raadt, computer geeft code",'\n',"2: Computer raadt, speler geeft code",'\n',"3: Stop spel")
    while True:
        keuze = int(input('Keuze: '))
        if keuze == 1:
            computercode()
        elif keuze == 2:
            spelercode()
        elif keuze == 3:
            break
        else:
            print('Probeer opnieuw')



def spelercode():
    antwoord = []
    while True:  # True todat user goede code geeft
        getallen = input("Geef een 4 cijferige code: ")
        if len(getallen) != 4:
            print('Probeer opnieuw')
        else:
            for getal in getallen:
                getal = int(getal)
                antwoord.append(getal)
            break
    algoritme(antwoord)

def computercode():
    antwoord = []
    for getal in range(4):
        los_getal = random.randrange(1, 7)
        antwoord.append(los_getal)
    spelerraad(antwoord)

def spelerraad(antwoord):
    print(''.join(antwoord))
    max_pogingen = 10 #max aantal pogingen
    aantal_pogingen = 0 #aantal pogingen dat de speler heeft gedaan

    for poging in range(max_pogingen):
        #print(poging)
        aantal_pogingen += 1
        print(aantal_pogingen)





menu()