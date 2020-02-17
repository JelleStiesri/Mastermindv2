from Feedback import feedback
from generate import gen
import random
eerst = [2,3,4,1]

def heuristiek(antwoord,lijst):
    tijd = 0
    gok = [1,1,1,1] #eerste gok
    f1 = feedback(gok,antwoord)
    zwart, wit = feedback(gok,antwoord)
    tijd += 1
    print("{}e feedback:".format(tijd),f1, gok)

    if f1 == (4,0):
        print('in 1 keer')
        oplossing = gok
        return oplossing, tijd

    totaal1 = zwart+wit
    aantal1 = zwart+wit
    gok = []
    for keer in range(totaal1):
        gok.append(1)
    tweetjes = 4 - totaal1
    for keer in range(tweetjes):
        gok.append(2)

    f2 = feedback(gok,antwoord)
    zwart, wit = feedback(gok, antwoord)
    tijd += 1
    print("{}e feedback:".format(tijd),f2, gok)

    if f1 == (4,0):
        print('in 1 keer')
        oplossing = gok
        return oplossing, tijd

    totaal2 = zwart + wit
    gok = []

    for keer in range(aantal1):
        gok.append(1)
    aantal2 = totaal2 - totaal1
    for keer in range(aantal2):
        gok.append(2)

    print(gok)




















    oplossing = 0

    return oplossing, tijd





def test(eerst):  #Test de gemiddelde snelheid
    pogingen = 1 # Verander deze om de gemiddelde snelheid te berekenen voor een bepaald aantal keer
    keer = 0
    totaal = 0
    maxi = []
    lst = gen()
    while keer != pogingen:
        ans, tijd = heuristiek(eerst,lst) #random.choice(lst)
        maxi.append(tijd)
        keer += 1
        totaal += tijd
    print()
    print('gem:',totaal/keer)
    print('max:', max(maxi))

test(eerst)