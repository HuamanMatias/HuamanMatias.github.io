import random

vida = 2 

for i in range(5):
    print("inicio vidas:", vida)
    jugador = random.randint(2,14)
    rival = random.randint(2,14)
    print("juagdor:", jugador, "rival:", rival)

    if jugador > rival:
        print("victoria")
    else:
        if jugador < rival:
            print("perdiste")
            vida = vida - 1
        else:
            print ("empate")
if vida == 0:
    print("as perdido todas tus vidas")