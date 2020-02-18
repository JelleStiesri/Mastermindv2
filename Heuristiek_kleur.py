from Feedback import feedback

def kleur(antwoord):
    print('Antwoord:',antwoord)
    tijd = 0
    gok = [1,1,1,1] #eerste gok

    f1 = feedback(gok,antwoord)
    zwart, wit = feedback(gok,antwoord)
    tijd += 1
    print("{}e feedback:".format(tijd),f1, gok)

    if f1 == (4,0):
        print('in 1 keer')
        return gok, f1, tijd

    totaal_feedback1 = zwart + wit
    aantal1 = totaal_feedback1

    # =============================

    gok2 = []
    tijd += 1
    for keer in range(aantal1):
        gok2.append(1)
    test2 = 4 - aantal1
    for keer in range(test2):
        gok2.append(2)
    feedback2 = backk(gok2, antwoord, tijd)

    totaal_feedback2 = sum(feedback2)
    aantal2 = totaal_feedback2-totaal_feedback1

    if totaal_feedback2 == 4:
        return gok, feedback2, tijd

    # =============================

    gok3 = []
    tijd += 1
    for keer in range(aantal1):
        gok3.append(1)
    for keer in range(aantal2):
        gok3.append(2)
    test3 = 4 - totaal_feedback2
    for keer in range(test3):
        gok3.append(3)
    feedback3 = backk(gok3, antwoord, tijd)

    totaal_feedback3 = sum(feedback3)
    aantal3 = totaal_feedback3 - totaal_feedback2

    if totaal_feedback3 == 4:
        return gok, feedback3, tijd
    # =============================

    gok4 = []
    tijd += 1
    for keer in range(aantal1):
        gok4.append(1)
    for keer in range(aantal2):
        gok4.append(2)
    for keer in range(aantal3):
        gok4.append(3)
    test4 = 4 - totaal_feedback3
    for keer in range(test4):
        gok4.append(4)
    feedback4 = backk(gok4, antwoord, tijd)

    totaal_feedback4 = sum(feedback4)
    aantal4 = totaal_feedback4 - totaal_feedback3

    if totaal_feedback4 == 4:
        return gok, feedback4, tijd
    # =============================

    gok5 = []
    tijd += 1
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
    feedback5 = backk(gok5, antwoord, tijd)

    totaal_feedback5 = sum(feedback5)
    aantal5 = totaal_feedback5 - totaal_feedback4

    if totaal_feedback5 == 4:
        return gok, feedback5, tijd
    # =============================

    gok6 = []
    tijd += 1
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
    feedback6 = backk(gok6, antwoord, tijd)

    totaal_feedback6 = sum(feedback6)
    aantal6 = totaal_feedback6 - totaal_feedback5

    if totaal_feedback6 == 4:
        return gok, feedback6, tijd
    else:
        return('ERROR')

def backk(gok, antwoord,tijd):
    back = feedback(gok, antwoord)
    print("{}e feedback:".format(tijd), back, gok)
    return(back)

#kleur([1,2,3,4])