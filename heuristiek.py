from Feedback import feedback
from generate import gen
import itertools
import random
from beste_gok import aanroep_best
from Heuristiek_kleur import kleur

""""
            INFO
        Zelf gemaatk algoritme (Totaal niet efficient natuurlik)
        Het programma zoekt eerst alle kleuren die in de code zitten en probeert daarna achter de volgorde te komen
"""
"""Bronnen:

"""
def algoritme(antwoord):
    kleuren, nieuwe_feedback, pogingen = kleur(antwoord)
    print(kleuren, nieuwe_feedback,pogingen)
    combi_lijst = combinaties(kleuren,nieuwe_feedback)

    gok = aanroep_best(combi_lijst)
    print(gok)

    input('doorgaan')
    while nieuwe_feedback != (4,0) and len(combi_lijst) != 1:
        print('len',len(combi_lijst))
        pogingen += 1
        gok = random.choice(combi_lijst)
        nieuwe_feedback = feedback(gok,antwoord)
        print("{}e feedback:".format(pogingen), nieuwe_feedback, gok, len(combi_lijst))
        combi_lijst = vergelijken(combi_lijst,kleuren,nieuwe_feedback)
        input('doorgaan')
    if nieuwe_feedback == (4,0):
        print('JEEEEJ')


def vergelijken(combi_lijst, gok, oude_feedback):
    nieuwe_lijst = [] #Tijdelijk
    for combinatie in combi_lijst:
        nieuwe_feedback = feedback(combinatie, gok)
        if nieuwe_feedback == oude_feedback:
            nieuwe_lijst.append(combinatie)
    combi_lijst = nieuwe_lijst
    return combi_lijst


def combinaties(gok, nieuwe_feedback):
    combis = []
    it = list(itertools.permutations(gok))
    for combinatie in it:
        leeg = []
        for nummer in combinatie:
            leeg.append(nummer)
        combis.append(leeg)
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
                #print('hoi')
                combis.remove(combinatie)
        print(combis)
        return combis
    else:
        print(combis)
        return combis


def backk(gok, antwoord,tijd):
    back = feedback(gok, antwoord)
    print("{}e feedback:".format(tijd), back, gok)
    return(back)


lst = gen()
algoritme(random.choice(lst))




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
#lst = gen()
#algoritme_uitvoering([3,2,3,4])




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

#test(eerst)


"""def algoritme_uitvoering(antwoord):
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


    
    totaal = zwart + wit
    #lijst met overige kleuren:
    if totaal == 4:
        print('Alle kleuren zijn geraden')
        combinaties(gok, nieuwe_feedback)
    else:
        print('Foutjeee')"""