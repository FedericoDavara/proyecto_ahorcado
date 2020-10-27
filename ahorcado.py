from servicesPartidas import ServicesPartidas

a = ServicesPartidas ()

print("¡¡Bienbenido al juego del ahoracado!!")

cantidadjugadores= int(input("Ingrese si es uno o dos jugadores: "))
if cantidadjugadores == 1:
    ServicesPartidas.iniciar_partida_palabra_random(a)
else:
    for i in range (2):
        print("Es el turno del jugador '{}'".format(i+1))
        ServicesPartidas.iniciar_partida(a)

