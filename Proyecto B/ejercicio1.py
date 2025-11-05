VidasJugador = int(input("Cuantas vidas quiere tener? "))
if VidasJugador >= 5:
    Dificultad = "Facil"
if VidasJugador in (4, 3):
    Dificultad = "Medio"
if VidasJugador  <= 2:
    Dificultad = "Dificil"

print("Tu dificultad sera:", Dificultad)