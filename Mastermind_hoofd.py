import random
from Raad_algoritme import algoritme
from Raad_speler import spelerraad
from heuristiek import heuristiek

def menu():
    while True:
        print("welke spelmodus wil je spelen",
              '\n', "1: Speler raadt, computer geeft code",
              '\n',"2: Computer raadt, speler geeft code",
              '\n', "3: Stop spel")
        keuze = int(input('Keuze: '))
        if keuze == 1:
            computercode()
        elif keuze == 2:
            spelercode()
        elif keuze == 3:
            print('Bedankt voor het spelen!')
            break
        else:
            print('Probeer opnieuw')

def spelercode(): #FIXEN DAT GETALLEN ONDER 7 ZIJN
    while True:  # True todat user goede code geeft
        antwoord = []
        getallen = input("Geef een 4 cijferige code: ")
        if getallen.isdigit() == True: #kijkt of de code uit cijfers bestaat
            if len(getallen) != 4:
                print('Probeer opnieuw')
                continue
            else:
                for getal in getallen:  # Zet alle getallen in een list
                    getal = int(getal)
                    antwoord.append(getal)
            if max(antwoord) > 6: #Checkt of de getallen niet groter zijn dan 6 (== 6 kleuren)
                print('De getallen mogen niet groter zijn dan 6')
                continue
            break
        print('De code mag alleen cijfers bevatten')

    while True:
        print("Welk algoritme wil je gebruiken",
              '\n', "1: Bewezen algoritme",
              '\n', "2: Heuristiek")
        keuze = int(input('Keuze: '))
        if keuze == 1:
            algoritme(antwoord)
        elif keuze == 2:
            heuristiek(antwoord)
        break

    """Heuristiek erbij"""

def computercode():
    antwoord = []
    for getal in range(4):
        los_getal = random.randrange(1, 7) #Genereert 4 getallen tussen de 1 en 6
        antwoord.append(los_getal)
    spelerraad(antwoord)

menu()