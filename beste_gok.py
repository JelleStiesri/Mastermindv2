from Feedback import feedback
from generate import gen

"""Bronnen:
        https://github.com/nattydredd/Mastermind-Five-Guess-Algorithm (Alleen de Readme, geen stukken code)
         YET ANOTHER MASTERMIND STRATEGY, Barteld Kooi, Universiteit van Groningen (algoritme 2.2)
     """

def beste_move(combi_lijst):
    dic = {}
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

def aanroep_best(combi_lijst):
    return beste_move(combi_lijst)

