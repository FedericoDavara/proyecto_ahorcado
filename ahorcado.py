from servicesPartidas import ServicesPartidas

a = ServicesPartidas ()

print("¡¡Bienbenido al juego del ahoracado!!")

cantidadjugadores= int(input("Ingrese si es uno o dos jugadores: "))
if cantidadjugadores == 1:
    ServicesPartidas.iniciar_partida_palabra_random(a)
else:
    ServicesPartidas.iniciar_partida(a)

