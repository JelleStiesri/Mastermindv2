from Feedback import feedback
from generate import gen
"""Functie/algoritme die de beste volgende stap berekend ('minimax' of het algoritme van 'Donald Knuth')

        Het heeft heel veel tijd gekost om dit goed te krijgen, de algoritmes worden er gemiddeld 0.1 zet sneller van dus daar lijkt hij het niet erg op te verbeteren.
        Wel gaat het maximaal aantal gokken naar 6 en zal hij dus nooit meer stappen nodig hebben dan dat. 
        In het originele algoritme (en algoritmes die mensen hebben gemaakt die veel beter kunnen programeren) is het maximale aantal 5, hij is dus niet optimaal efficient.

    Gebruikte andere functies: feedback """
"""Bronnen:
        https://github.com/nattydredd/Mastermind-Five-Guess-Algorithm (Alleen de Readme, geen stukken code)
         YET ANOTHER MASTERMIND STRATEGY, Barteld Kooi, Universiteit van Groningen (algoritme 2.2)
     """

def beste_move(combi_lijst):
    dic = dict((min(combi_lijst, combinatie), combinatie) for combinatie in combi_lijst) #maakt een dict met aantal eliminaties als key
    maximaal = max(dic.keys()) #Geeft de combinatie waarbij het maximaal aantal andere combis worden geelimineerd
    beste = dic[maximaal] #Dit is de volgende gok
    return beste

def min(combi_lijst, gok): #minimale aantal geelimineerde combi's
    totaal_resultaten = {}
    for combinatie in combi_lijst: #item = elke nog mogelijke combinatie
        nieuwe_feedback = feedback(combinatie, gok)
        if nieuwe_feedback not in totaal_resultaten.keys(): #kijkt of de specifieke feedback al in de dictionary staat
            totaal_resultaten[nieuwe_feedback] = 1 #Als de feedback nog niet in de dict staat maakt hij een niew item aan in de dict
        else:
            totaal_resultaten[nieuwe_feedback] += 1
    totaal = len(combi_lijst) - max(totaal_resultaten.values()) #returnt het aantal minimale aantal geelimineerde items van combilijst\
    return totaal

def aanroep_best(combi_lijst): #deze functie heeft niet veel nut maar is handig voor testen
    return beste_move(combi_lijst)