def spelercode(): #FIXEN DAT GETALLEN ONDER 7 ZIJN
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