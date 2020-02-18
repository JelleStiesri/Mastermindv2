from Feedback import feedback
from generate import gen
from beste_gok import aanroep_best
import random
""""
            INFO
        Dit algoritme is gebaseert op de paper van de Uni van groningen.
        Als basis heb ik het simpelste algoritme gebruikt. Ik heb deze uitgebreid -
        - door een 2e algoritme toe te voegen (degene die de beste volgende gok kiest)
        Het 2e algoritme komt van het principe 'minimax' of het algoritme van 'Donald Knuth'
        
        Gebruikte andere functies: beste_gok, feedback, generate
"""
"""Bronnen:
        YET ANOTHER MASTERMIND STRATEGY, Barteld Kooi, Universiteit van Groningen (algoritme 2.1)
        (Concept komt dan de paper, De code van mezelf)     
"""

def algoritme(antwoord):
    combi_lijst = gen() #Deze functie staat apart zodat het testen sneller kan gaan (Anders moet gen steeds opnieuw)
    oplossing, tijd =algoritme_uitvoering(antwoord,combi_lijst)
    return oplossing, tijd

def algoritme_uitvoering(antwoord,combi_lijst):
    tijd = 1
    gok = [1,1,2,3]  #Eerste gok, bewezen de snelste
    nieuwe_feedback = feedback(gok, antwoord) #Eerste feedback
    if nieuwe_feedback == (4, 0):
        print('Geraden in 1 zet! - Antwoord = ', gok, '\n')
        return gok, tijd
    print('Gok 1: {} -- Feedback: {}'.format(gok,nieuwe_feedback))

    while len(combi_lijst) != 1:
        tijd += 1
        combi_lijst = vergelijken(combi_lijst, gok, nieuwe_feedback)
        gok = aanroep_best(combi_lijst) #Voor algoritme 'beste gok'
        nieuwe_feedback = feedback(gok,antwoord)
        print('Gok {}: {} -- Feedback: {}'.format(tijd, gok, nieuwe_feedback))
        if nieuwe_feedback == (4,0):
            print('Aantal zetten', tijd, '---', 'Antwoord =', gok,'\n')
            return gok, tijd

    oplossing = combi_lijst[0]
    print('Aantal zetten', tijd, '---', 'Antwoord =', combi_lijst[0],'\n')
    return oplossing, tijd

def vergelijken(combi_lijst, gok, oude_feedback):
    nieuwe_lijst = [] #Tijdelijk
    for combinatie in combi_lijst:
        nieuwe_feedback = feedback(combinatie, gok)
        if nieuwe_feedback == oude_feedback:
            nieuwe_lijst.append(combinatie)
    combi_lijst = nieuwe_lijst
    return combi_lijst

def test():  #Test de gemiddelde snelheid
    pogingen = 1500  # Verander deze om de gemiddelde snelheid te berekenen voor een bepaald aantal keer
    keer = 0
    totaal = 0
    maxi = []
    lst = gen()
    while keer != pogingen:
        ans, tijd = algoritme_uitvoering(random.choice(lst),lst) #random.choice(lst)
        maxi.append(tijd)
        keer += 1
        totaal += tijd
        print(keer)
    print('gem',totaal/keer)
    print('max:', max(maxi))

#test()