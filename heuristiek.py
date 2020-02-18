from Feedback import feedback
from generate import gen
import itertools
from beste_gok import aanroep_best
import random
""""
            INFO
        Dit algoritme is gebaseert op de paper van de Uni van groningen.
        Als basis heb ik het simpelste algoritme gebruikt. Ik heb deze uitgebreid -
        - door een 2e algoritme toe te voegen (degene die de beste volgende gok kiest)
        Het 2e algoritme komt van het principe 'minimax' of het algoritme van 'Donald Knuth'
"""
"""Bronnen:
        YET ANOTHER MASTERMIND STRATEGY, Barteld Kooi, Universiteit van Groningen (algoritme 2.1)
        (Concept komt dan de paper, De code van mezelf)     
"""


def algoritme(antwoord):
    combi_lijst = gen() #Deze functie staat apart zodat het testen sneller kan gaan (Anders moet gen steeds opnieuw)
    oplossing, tijd =algoritme_uitvoering(antwoord)
    return oplossing, tijd

def algoritme_uitvoering(antwoord):
    print('antwoord:', antwoord)
    tijd = 1
    gok = [2,3,4,3] #random.choice(combi_lijst)  #Eerste gok
    nieuwe_feedback = feedback(gok, antwoord) #Eerste feedback
    zwart, wit = feedback(gok, antwoord)
    if nieuwe_feedback == (4, 0):
        print('Geraden in 1 zet! - Antwoord = ', gok, '\n')
        return gok, tijd
    print('Gok 1: {} -- Feedback: {}'.format(gok,nieuwe_feedback))
    print("=================================================")


    """Kleur raden"""
    totaal = zwart + wit
    #lijst met overige kleuren:
    if totaal == 4:
        print('Alle kleuren zijn geraden')
        combinaties(gok, nieuwe_feedback)
    else:
        print('Foutjeee')

def combinaties(gok, nieuwe_feedback):
    combis = []
    it = list(itertools.permutations(gok))
    for combinatie in it:
        leeg = []
        for nummer in combinatie:
            leeg.append(nummer)
        if leeg not in combis:
            combis.append(leeg)
    #print(combis,'\n')

    if nieuwe_feedback == (0,4):
        combis2 = []
        for combinatie in combis: #Deze 4 zijn blijkbaar nodig om alles er uit te filteren
            if combinatie[0] == gok[0]: #is gok[0] or combinatie[1] is gok[1] or combinatie[2] is gok[2] or combinatie[3] is gok[3]:
                #print(combinatie,combinatie[0], gok[0])
                combis.remove(combinatie)
        for combinatie in combis:
            if combinatie[1] == gok[1]:
                #print(combinatie,combinatie[1], gok[1])
                combis.remove(combinatie)
        for combinatie in combis:
            if combinatie[2] == gok[2]:
                #print(combinatie,combinatie[2], gok[2])
                combis.remove(combinatie)
        for combinatie in combis:
            if combinatie[3] == gok[3]:
                #print(combinatie,combinatie[3], gok[3])
                combis.remove(combinatie)
        for combinatie in combis: #Zonder deze word niet alles er uit gefiltert
            if combinatie[0] == gok[0] or combinatie[1] == gok[1] or combinatie[2] == gok[2] or combinatie[3] == gok[3]:
                combis.remove(combinatie)
        print(combis)
        print(aanroep_best(combis))












"""oplossing = combi_lijst[0]
    print('Aantal zetten', tijd, '---', 'Antwoord =', combi_lijst[0],'\n')
    return oplossing, tijd"""





def test():  #Test de gemiddelde snelheid
    pogingen = 1  # Verander deze om de gemiddelde snelheid te berekenen voor een bepaald aantal keer
    keer = 0
    totaal = 0
    maxi = []
    lst = gen()
    while keer != pogingen:
        ans, tijd = algoritme_uitvoering([]) #random.choice(lst)
        maxi.append(tijd)
        keer += 1
        totaal += tijd
        print(keer)
    print('gem',totaal/keer)
    print('max:', max(maxi))

#test()
lst = gen()
algoritme_uitvoering([3,2,3,4])









"""from Feedback import feedback
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

test(eerst)"""