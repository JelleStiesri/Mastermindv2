from generate import gen
import random
from collections import Counter
from Feedback import feedback

vaste_lijst = gen() # In deze lijst veranderd niks


def minimax(antwoord,lijst):
    print("Antwoord: ",antwoord)
    #lijst = gen Na het testen word dit gebruikt
    tijd = 0
    time = 0

    gok = [1,1,2,2] #Eerste gok
    nieuwe_feedback = 0

    while nieuwe_feedback != (4,0):
        tijd += 1
        nieuwe_feedback = feedback(gok,antwoord)
        print('Gok {}: {} -- Feedback: {}'.format(tijd, gok, nieuwe_feedback))
        if nieuwe_feedback == (4,0):
            break

        tijdelijke_lijst = lijst
        lijst = []
        for combinatie in tijdelijke_lijst:
            if feedback(gok,combinatie) == nieuwe_feedback: #lijkt of de feedback tussen oude gok en item in lijst zelfde is als nieuwe feedback
                 lijst.append(combinatie)
        print('lengte', len(lijst))
        if len(lijst) == 1:
            gok = lijst[0]
        else:
            gok = min(vaste_lijst, key = lambda g: max(Counter(feedback(g, c) for c in lijst).values())) #"""BRON"""


    print('\n', 'Aantal zetten', tijd, '---', 'Antwoord =', gok, )
    print('tijd', tijd)
    return gok, tijd



def tellen(feed): #
    dic = {}
    for item in feed:

        try:
            dic[item] += 1
            #print('normaal')
        except KeyError: #wanneer de key nog niet bestaat
            dic[item] = 1
        print(dic)


            #print('eroroor')


    return dic













minimax([1,5,3,6],vaste_lijst) #random.choice(vaste_lijst)


def test():  #Test de gemiddelde snelheid
    pogingen = 1 # Verander deze om de gemiddelde snelheid te berekenen voor een bepaald aantal keer
    keer = 0
    totaal = 0
    maxi = []
    lst = gen()
    while keer != pogingen:
        print(keer)
        ans, tijd = minimax(random.choice(lst),lst) #random.choice(lst)
        maxi.append(tijd)
        keer += 1
        totaal += tijd
    print('gem',totaal/keer)
    print('max:', max(maxi))

#test()
