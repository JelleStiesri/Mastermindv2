while len(combi_lijst) != 1:
    nieuwe_lijst = []

    for combinatie in combi_lijst:
        nieuwe_feedback = feedback(combinatie, nieuwe_gok)
        """print('Gok: ',gok)
        print('eerste feedback: ',nieuwe_feedback)
        print("lengte van lijst (0): ", len(combi_lijst))
        print('--------------------------------')"""
        if nieuwe_feedback == oude_feedback:
            nieuwe_lijst.append(combinatie)
            print(combinatie, nieuwe_feedback)
        else:
            combi_lijst.remove(combinatie)
    combi_lijst = nieuwe_lijst
    oude_feedback = nieuwe_feedback
    print("lengte van lijst: ", len(combi_lijst))

    nieuwe_gok = random.choice(combi_lijst)
    oude_feedback = feedback(nieuwe_gok, antwoord)
    print(nieuwe_gok, oude_feedback)

import itertools










"""import random
def gen():
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
            print('klaar')
            break
    lijst.sort(key=lambda x: x[0])


    print(lijst,'\nlengte:',len(lijst),'\nkeren opnieuw:',fout)

gen()"""




