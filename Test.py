from Feedback import feedback


def kleur(antwoord):
    tijd = 0
    gok = [1,1,1,1] #eerste gok
    f1 = feedback(gok,antwoord)
    zwart, wit = feedback(gok,antwoord)
    tijd += 1
    print("{}e feedback:".format(tijd),f1, gok)

    # =============================
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
    totaal2 = zwart + wit
    aantal2 = totaal2 - totaal1
    tijd += 1
    print("{}e feedback:".format(tijd),f2, gok)

    if f2 == (4,0):
        print('in 1 keer')
        oplossing = gok
        return oplossing, tijd

    # =============================
    totaal3 = zwart + wit
    aantal3 = zwart + wit
    gok = []
    for keer in range(totaal1):
        gok.append(1)
    for keer in range(aantal2):
        gok.append(2)
    drietjes = 4 - totaal3
    for keer in range(drietjes):
        gok.append(3)

    f3 = feedback(gok, antwoord)
    zwart, wit = feedback(gok, antwoord)
    tijd += 1
    print("{}e feedback:".format(tijd), f3, gok)

    if f3 == (4,0):
        print('in 1 keer')
        oplossing = gok
        return oplossing, tijd

    # =============================
    totaal4 = zwart + wit
    aantal4 = totaal4-drietjes
    gok = []
    for keer in range(totaal1):
        gok.append(1)
    for keer in range(aantal2):
        gok.append(2)
    for keer in range(drietjes):
        gok.append(3)
    viertjes = 4 - totaal4
    for keer in range(viertjes):
        gok.append(4)
    print(gok)

    f4 = feedback(gok, antwoord)
    zwart, wit = feedback(gok, antwoord)
    tijd += 1
    print("{}e feedback:".format(tijd), f4, gok)

    if f4 == (4, 0):
        print('in 1 keer')
        oplossing = gok
        return oplossing, tijd





kleur([3,2,1,6])