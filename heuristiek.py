from Feedback import feedback
from generate import gen
import itertools
import random
from beste_gok import aanroep_best
from Heuristiek_kleur import kleur

""""
            INFO
        Zelf gemaatk algoritme (Totaal niet efficient natuurlik)
        Het programma zoekt eerst alle kleuren die in de code zitten en probeert daarna achter de volgorde te komen doormiddel van het basisalgoritme
        
        Gebruikte andere functies: beste_gok, feedback, generate, heuristiek_kleur 
"""
def heuristiek(antwoord):
    kleuren, nieuwe_feedback, pogingen = kleur(antwoord)
    combi_lijst = combinaties(kleuren,nieuwe_feedback)
    gok = aanroep_best(combi_lijst)
    nieuwe_feedback = feedback(gok,antwoord)
    pogingen += 1
    if nieuwe_feedback == (4, 0):
        print('Aantal zetten', pogingen, '---', 'Antwoord =', gok,'\n')
        return gok, pogingen
    print('Gok {}: {} -- Feedback: {}'.format(pogingen, gok, nieuwe_feedback))

    while pogingen != 10:
        pogingen += 1
        combi_lijst = vergelijken(combi_lijst,gok,nieuwe_feedback)
        gok = aanroep_best(combi_lijst)
        nieuwe_feedback = feedback(gok,antwoord)
        print('Gok {}: {} -- Feedback: {}'.format(pogingen, gok, nieuwe_feedback))
        if nieuwe_feedback == (4,0):
            print('Aantal zetten', pogingen, '---', 'Antwoord =', gok,'\n')
            return gok, pogingen

    print('De computer heeft verloren!','\n')

def vergelijken(combi_lijst, gok, oude_feedback):
    nieuwe_lijst = []  # Tijdelijk
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
        return combis
    else:
        return combis

def backk(gok, antwoord,pogingen):
    nieuwe_feedback = feedback(gok, antwoord)
    print('Gok {}: {} -- Feedback: {}'.format(pogingen, gok, nieuwe_feedback))
    return(nieuwe_feedback)