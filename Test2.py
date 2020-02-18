from Feedback import feedback


def kleur(antwoord):
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
    # =============================
    totaal_feedback1 = zwart + wit
    aantal1 = totaal_feedback1

    gok 








kleur([3,2,1,6])