from generate import gen
from Feedback import feedback
from collections import Counter
import random

def knuth(secret,lijst):
    """Run Knuth's 5-guess algorithm on the given secret."""
    tijd = 0
    print('code:', secret)
    #assert(secret in lijst)
    codes = lijst

    key = lambda g: max(Counter(feedback(g, c) for c in codes).values())


            guess = min(lijst, key=key)



def test():  #Test de gemiddelde snelheid
    pogingen = 2 # Verander deze om de gemiddelde snelheid te berekenen voor een bepaald aantal keer
    keer = 0
    totaal = 0
    maxi = []
    lst = gen()
    while keer != pogingen:
        print(keer)
        ans, tijd = knuth(random.choice(lst),lst) #random.choice(lst)
        maxi.append(tijd)
        keer += 1
        totaal += tijd
    print('gem',totaal/keer)
    print('max:', max(maxi))

test()