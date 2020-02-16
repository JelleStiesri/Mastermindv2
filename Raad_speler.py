from Feedback import feedback
def spelerraad(antwoord):
    print(antwoord) #Weghalen tijdens oplevering
    max_pogingen = 3 #max aantal pogingen
    aantal_pogingen = 0 #aantal pogingen dat de speler heeft gedaan
    ans = False
    gok = 0
    while gok != antwoord and aantal_pogingen != max_pogingen:
        aantal_pogingen += 1
        gok = gok_code(aantal_pogingen)
        zwart, wit = feedback(gok,antwoord)
        print('Zwart: {} - Wit: {}'.format(zwart,wit))

    if gok == antwoord:
        print('Je hebt gewonnen!')
        print('Aantal zetten: ', aantal_pogingen, ' - ', 'Antwoord: ', *gok,sep='')
    elif aantal_pogingen == max_pogingen:
        print('Je hebt verloren!')
        print('Het antwoord was: ', *antwoord,sep='')


def gok_code(poging):
    while True:  # True todat user 4 cijferige code geeft
        gok = []
        getallen = input("{}e gok: ".format(poging))

        if len(getallen) != 4:
            print('Probeer opnieuw')
        else:
            for getal in getallen:
                getal = int(getal)
                gok.append(getal)
            return gok


spelerraad([1,5,6,7])