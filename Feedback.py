def feedback(gok, antwoord):
    zwart = zwart_feedback(gok,antwoord)
    wit = wit_feedback(gok, antwoord)
    wit = wit - zwart
    return zwart, wit


def zwart_feedback(gok, antwoord):
    index = 0
    zwart = 0
    for item in gok:
        if item == antwoord[index]: # kijkt of gok en antwoord zelfde zijn
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


def gok():
    gok = []
    while True:  # True todat user goede code geeft
        getallen = input("Gok: ")

        if len(getallen) != 4:
            print('Probeer opnieuw')
        else:
            for getal in getallen:
                getal = int(getal)
                gok.append(getal)
            break
    feedback(gok,[3, 7, 2, 3])
    #feedback(gok, [3, 7, 2, 3])


#print(feedback([1, 7, 3, 2], [3, 7, 2, 3]))


#while True:
#    gok()