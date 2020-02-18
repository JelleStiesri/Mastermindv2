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


def heuristiek(antwoord, lst):
    # lst = gen()
    kleuren, nieuwe_feedback, pogingen = kleur(antwoord)
    # print(kleuren, nieuwe_feedback,pogingen)
    combi_lijst = combinaties(kleuren, nieuwe_feedback)

    gok = aanroep_best(combi_lijst)
    nieuwe_feedback = feedback(gok, antwoord)
    print()
    pogingen += 1
    if nieuwe_feedback == (4, 0):
        print('Aantal zetten', pogingen, '---', 'Antwoord =', gok, '\n')
        return gok, pogingen
    print('Gok {}: {} -- Feedback: {}'.format(pogingen, gok, nieuwe_feedback))

    while len(combi_lijst) != 1:
        pogingen += 1
        combi_lijst = vergelijken(combi_lijst, gok, nieuwe_feedback)
        gok = aanroep_best(combi_lijst)
        nieuwe_feedback = feedback(gok, antwoord)
        print('Gok {}: {} -- Feedback: {}'.format(pogingen, gok, nieuwe_feedback))
        if nieuwe_feedback == (4, 0):
            print('Aantal zetten', pogingen, '---', 'Antwoord =', gok, '\n')
            return gok, pogingen

    oplossing = combi_lijst[0]
    print('Aantal zetten', pogingen, '---', 'Antwoord =', combi_lijst[0], '\n')
    return oplossing, pogingen


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

    if nieuwe_feedback == (0, 4):
        combis2 = []
        for combinatie in combis:  # Deze 4 zijn blijkbaar nodig om alles er uit te filteren
            if combinatie[0] == gok[
                0]:  # is gok[0] or combinatie[1] is gok[1] or combinatie[2] is gok[2] or combinatie[3] is gok[3]:
                # print(combinatie,combinatie[0], gok[0])
                combis.remove(combinatie)
        for combinatie in combis:
            if combinatie[1] == gok[1]:
                # print(combinatie,combinatie[1], gok[1])
                combis.remove(combinatie)
        for combinatie in combis:
            if combinatie[2] == gok[2]:
                # print(combinatie,combinatie[2], gok[2])
                combis.remove(combinatie)
        for combinatie in combis:
            if combinatie[3] == gok[3]:
                # print(combinatie,combinatie[3], gok[3])
                combis.remove(combinatie)
        for combinatie in combis:  # Zonder deze word niet alles er uit gefiltert
            if combinatie[0] == gok[0] or combinatie[1] == gok[1] or combinatie[2] == gok[2] or combinatie[3] == gok[3]:
                # print('hoi')
                combis.remove(combinatie)
        print(combis)
        return combis
    else:
        print(combis)
        return combis


def backk(gok, antwoord, tijd):
    back = feedback(gok, antwoord)
    print("{}e feedback:".format(tijd), back, gok)
    return (back)


# lst = gen()
# algoritme(random.choice(lst))

def test():  # Test de gemiddelde snelheid
    pogingen = 25000  # Verander deze om de gemiddelde snelheid te berekenen voor een bepaald aantal keer
    keer = 0
    totaal = 0
    maxi = []
    lst = gen()
    while keer != pogingen:
        ans, tijd = heuristiek(random.choice(lst), lst)  # random.choice(lst)
        maxi.append(tijd)
        keer += 1
        totaal += tijd
    print()
    print('gem:', totaal / keer)
    print('max:', max(maxi))


test()

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

test()
from Feedback import feedback
"""Functie die de speler de code laat gokken"""

def spelerraad(antwoord):
    print(antwoord) #Weghalen tijdens oplevering
    max_pogingen = 8
    aantal_pogingen = 0 #aantal pogingen dat de speler heeft gedaan
    ans = False
    gok = 0
    while gok != antwoord and aantal_pogingen != max_pogingen:
        aantal_pogingen += 1
        gok = gok_code(aantal_pogingen)
        zwart, wit = feedback(gok,antwoord)
        print('Zwart: {} - Wit: {}'.format(zwart,wit),'\n')

    if gok == antwoord:
        print('Je hebt gewonnen!')
        print('Aantal zetten: ', aantal_pogingen, ' - ', 'Antwoord: ', *gok,sep='')
        print()
    elif aantal_pogingen == max_pogingen:
        print('Je hebt verloren!')
        print('Het antwoord was: ', *antwoord,sep='')
        print()

def gok_code(poging):
    while True:  # True todat user 4 cijferige code geeft
        gok = []
        getallen = input("{}e gok: ".format(poging))

        if len(getallen) != 4:
            print('Probeer opnieuw','\n')
            continue
        else:
            for getal in getallen:
                getal = int(getal)
                gok.append(getal)
        if max(gok) >6:
            print('De getallen mogen niet groter zijn dan 6')
            continue
        else:
            return gok
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
"""Mijn feedback programma"""

def feedback(gok, antwoord):
    zwart = zwart_feedback(gok,antwoord)
    wit = wit_feedback(gok, antwoord)
    wit = wit - zwart
    return zwart, wit

def zwart_feedback(gok, antwoord):
    index = 0
    zwart = 0
    for item in gok:
        if item == antwoord[index]:
            zwart += 1
        index += 1
    return zwart

def wit_feedback(gok, antwoord):
    lijst = antwoord[:] #De ':' neemt alle antwoorden over in een andere lijst,
    wit = 0
    for item in gok:
        if item in lijst: #Dit voorkomt dat: feedback is 2,1 als je 3433 invult
            lijst.remove(item)
            wit += 1
    return wit

#print(feedback([1, 7, 3, 2], [3, 7, 2, 3])) #Om te testen
import random
"""Deze functie maakt alle mogelijke combinaties"""
def gen(): # Maakt een lijst met alle mogelijke combinaties van de cijfers 1/6 en met 4 tekens te gelijk
    lijst = []
    fout = 0
    while True:
        combinatie = []
        for getal in range(4):
            los_getal = random.randrange(1, 7)
            combinatie.append(los_getal)
        if combinatie in lijst:
            fout = fout + 1
            continue
        else:
            lijst.append(combinatie)
        if len(lijst) == 1296: #aantal mogelijke combinaties
            break
    lijst.sort(key=lambda x: x[0]) #sorteert alleen op eerste karakter in lijst, verder is niet nodig
    return(lijst)
from Feedback import feedback

"""Deze functie zoekt welke kleuren er in de code staan, Dit is onderdeel van het zelfbedachte heuristiek

    Hij begint met 1111, uit deze feedback kan je afleiden hoeveel 1en erin zitten, de rest vul je op met 2. 
    De hoeveelheid totale pinnetjes die erbij komen (ten opzichte van eerste feedback) staat gelijk aan het aantal 2en in de code. 
    Dit doe ik tot en met 6 zodat je weet welke kleuren erin zitten
"""



def kleur(antwoord):
    print('Antwoord:',antwoord)
    pogingen = 0
    gok = [1,1,1,1] #eerste gok

    f1 = feedback(gok,antwoord)
    zwart, wit = feedback(gok,antwoord)
    pogingen += 1
    print("{}e feedback:".format(pogingen),f1, gok)

    if f1 == (4,0):
        print('in 1 keer')
        return gok, f1, pogingen

    totaal_feedback1 = zwart + wit
    aantal1 = totaal_feedback1

    # =============================

    gok2 = []
    pogingen += 1
    for keer in range(aantal1):
        gok2.append(1)
    test2 = 4 - aantal1
    for keer in range(test2):
        gok2.append(2)
    feedback2 = backk(gok2, antwoord, pogingen)

    totaal_feedback2 = sum(feedback2)
    aantal2 = totaal_feedback2-totaal_feedback1

    if totaal_feedback2 == 4:
        gok = gok2
        return gok, feedback2, pogingen

    # =============================

    gok3 = []
    pogingen += 1
    for keer in range(aantal1):
        gok3.append(1)
    for keer in range(aantal2):
        gok3.append(2)
    test3 = 4 - totaal_feedback2
    for keer in range(test3):
        gok3.append(3)
    feedback3 = backk(gok3, antwoord, pogingen)

    totaal_feedback3 = sum(feedback3)
    aantal3 = totaal_feedback3 - totaal_feedback2

    if totaal_feedback3 == 4:
        gok = gok3
        return gok, feedback3, pogingen
    # =============================

    gok4 = []
    pogingen += 1
    for keer in range(aantal1):
        gok4.append(1)
    for keer in range(aantal2):
        gok4.append(2)
    for keer in range(aantal3):
        gok4.append(3)
    test4 = 4 - totaal_feedback3
    for keer in range(test4):
        gok4.append(4)
    feedback4 = backk(gok4, antwoord, pogingen)

    totaal_feedback4 = sum(feedback4)
    aantal4 = totaal_feedback4 - totaal_feedback3

    if totaal_feedback4 == 4:
        gok = gok4
        return gok, feedback4, pogingen
    # =============================

    gok5 = []
    pogingen += 1
    for keer in range(aantal1):
        gok5.append(1)
    for keer in range(aantal2):
        gok5.append(2)
    for keer in range(aantal3):
        gok5.append(3)
    for keer in range(aantal4):
        gok5.append(4)
    test5 = 4 - totaal_feedback4
    for keer in range(test5):
        gok5.append(5)
    feedback5 = backk(gok5, antwoord, pogingen)

    totaal_feedback5 = sum(feedback5)
    aantal5 = totaal_feedback5 - totaal_feedback4

    if totaal_feedback5 == 4:
        gok = gok5
        return gok, feedback5, pogingen
    # =============================

    gok6 = []
    pogingen += 1
    for keer in range(aantal1):
        gok6.append(1)
    for keer in range(aantal2):
        gok6.append(2)
    for keer in range(aantal3):
        gok6.append(3)
    for keer in range(aantal4):
        gok6.append(4)
    for keer in range(aantal5):
        gok6.append(5)
    test6 = 4 - totaal_feedback5
    for keer in range(test6):
        gok6.append(6)
    feedback6 = backk(gok6, antwoord, pogingen)

    totaal_feedback6 = sum(feedback6)

    if totaal_feedback6 == 4:
        gok = gok6
        return gok, feedback6, pogingen
    else:
        return('ERROR')


def backk(gok, antwoord,pogingen):
    back = feedback(gok, antwoord)
    print("{}e feedback:".format(pogingen), back, gok)
    return(back)

#kleur([1,2,3,4])
import random
from Raad_algoritme import algoritme
from Raad_speler import spelerraad

def menu():
    antwoord = []
    while True:
        print("welke spelmodus wil je spelen",
              '\n', "1: Speler raadt, computer geeft code",
              '\n',"2: Computer raadt, speler geeft code",
              '\n', "3: Stop spel")
        keuze = int(input('Keuze: '))
        if keuze == 1:
            computercode()
        elif keuze == 2:
            spelercode()
        elif keuze == 3:
            print('Bedankt voor het spelen!')
            break
        else:
            print('Probeer opnieuw')

def spelercode(): #FIXEN DAT GETALLEN ONDER 7 ZIJN
    while True:  # True todat user goede code geeft
        antwoord = []
        getallen = input("Geef een 4 cijferige code: ")
        print()
        if len(getallen) != 4:
            print('Probeer opnieuw')
            continue
        else:
            for getal in getallen: #Zet alle getallen in een list
                getal = int(getal)
                antwoord.append(getal)
        if max(antwoord) > 6: #Checkt of de getallen niet groter zijn dan 6 (== 6 kleuren)
            print('De getallen mogen niet groter zijn dan 6')
            continue
        algoritme(antwoord)
        break

    """Heuristiek erbij"""

def computercode():
    antwoord = []
    for getal in range(4):
        los_getal = random.randrange(1, 7) #Genereert 4 getallen tussen de 1 en 6
        antwoord.append(los_getal)
    spelerraad(antwoord)

menu()






