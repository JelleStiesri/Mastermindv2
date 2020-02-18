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