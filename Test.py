from Feedback import feedback

def heuristiek(antwoord,lijst):
    tijd = 0
    gok = [1,1,1,1] #eerste gok
    f1 = feedback(gok,antwoord)
    zwart, wit = feedback(gok,antwoord)
    tijd += 1
    print("{}e feedback:".format(tijd),f1, gok)

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
    tijd += 1
    print("{}e feedback:".format(tijd),f2, gok)

    if f1 == (4,0):
        print('in 1 keer')
        oplossing = gok
        return oplossing, tijd

    totaal2 = zwart + wit
    gok = []

    for keer in range(aantal1):
        gok.append(1)
    aantal2 = totaal2 - totaal1
    for keer in range(aantal2):
        gok.append(2)

    print(gok)