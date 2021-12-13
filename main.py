"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""
from random import randrange

randomSzam = randrange(1,3)
print("Adj meg egy számot")
bemenet = int(input())
if bemenet == randomSzam:
    print("A kétszám egyezik. ")
elif bemenet > randomSzam:
    print("Az általad megadot szám nagyob , mint a random szám")
else:
    print("Az általad megadott szám kiseb, mint a random szám")