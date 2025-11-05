import random

def dicerollp1():
    num1p1 = random.randint(0,6)
    num2p1 = random.randint(0,6)
    num3p1 = random.randint(0,6)
    power = num1p1 + num2p1 + num3p1
    return power

def dicerollp2():
    num1p2 = random.randint(0,6)
    num2p2 = random.randint(0,6)
    num3p2 = random.randint(0,6)
    power = num1p2 + num2p2 + num3p2
    return power

turn = random.randint(1, 2)
hpp1 = 50
hpp2 = 50
while(hpp1 > 0 and hpp2 > 0):
    if turn == 1:
        print("Jugador 1, presione una tecla para tirar los dados")
        input()
        dmg1 = dicerollp1()
        print("Jugador 2 recibe: ", dmg1, " de daño...")
        print(hpp1)
        hpp2 = hpp2 - dmg1
        turn = 2
    if turn == 2:
        print("Jugador 2, presione una tecla para tirar los dados")
        input()
        dmg2 = dicerollp2()
        print("Jugador 1 recibe: ", dmg2, " de daño...")
        hpp1 = hpp1 - dmg2
        print(hpp2)
        turn = 1
if hpp1 <= 0:
    print("Ganador Jugador 2")
    input()
if hpp2 <= 0:
    print("Ganador Jugador 1")
    input()