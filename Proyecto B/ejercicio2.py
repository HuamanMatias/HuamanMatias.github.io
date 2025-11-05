import random

tiradasUsuario = int(input("¿Cuantas tiradas de dados quieres realizar? "))
contadorTiradas = 0
puntaje = 0

while(contadorTiradas < tiradasUsuario):
    contadorTiradas = contadorTiradas + 1
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    puntaje += dado1 + dado2
    print('dado 1:', dado1, 'y', 'dado 2:', dado1 )

print("El puntaje obtenido es de:", puntaje)