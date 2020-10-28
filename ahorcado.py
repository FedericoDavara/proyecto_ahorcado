from servicesPartidas import ServicesPartidas
from repositorios import Repositorios


class Ahorcado():
    def un_jugador(self):
        gano = 'Gano'
        salida = 'salir'
        try:
            estado = True
            servPart = ServicesPartidas()
            nombre_jugador = input('Ingresa Tu Nombre: ')
            while True:
                try:
                    dificultad = int(input('Elije dificultad 1 a 10 '))
                    partida0 = servPart.iniciar_partida(nombre_jugador,
                                                        dificultad, '', '')
                    break
                except Exception:
                    print('Error, dificultad no valida')
            print('Okey empecemos, tu palabra a adivinar es de tipo',
                  partida0.tipo_palabra)
            print('Primer y ultima letra', partida0.palabra[0], '-',
                  partida0.palabra[-1])
            for _ in range(0, partida0.intentos):
                letra = input('Ingrese letra: ')
                resultado = servPart.intentar_letra(partida0, letra)
                print(partida0.palabra_aciertos)
                print('Te quedan', partida0.intentos, 'intentos')
                print(partida0.nombre_jugador, resultado)
                if letra == salida:
                    break
                if resultado == gano:
                    break
            while estado:
                condicion = input('Quieres volver a jugar?(s/n): ')
                if condicion == 's':
                    self.un_jugador()
                if condicion == 'n':
                    estado = False
                else:
                    print('Error, entrada erronea :/')

        except Exception:
            StopIteration
        return True

    def dos_jugadores(self):
        gano = 'Gano'
        salida = 'salir'
        try:
            estado1 = True
            estado2 = True
            estado3 = True
            while estado1:
                servPart = ServicesPartidas()
                while True:
                    try:
                        jugadador1 = input('Turno del Jugador 1,tu nombre?: ')
                        dificultad1 = int(input('Que dificultad'
                                                ' eliges? (1-10): '))
                        palabra1 = input('Ingresa la palabra a adivinar: ')
                        tipoPalabra1 = input('Ingresa el tipo de palabra: ')
                        partida1 = servPart.iniciar_partida(jugadador1,
                                                            dificultad1,
                                                            palabra1,
                                                            tipoPalabra1)
                        break
                    except Exception:
                        print('Dificultad erronea :/')
                print('Llego la hora de adivinar!')
                for _ in range(0, partida1.intentos):
                    letra1 = input('Ingrese letra: ')
                    resultado = servPart.intentar_letra(partida1, letra1)
                    print(partida1.palabra_aciertos)
                    print('Te quedan', partida1.intentos, 'intentos')
                    print(partida1.nombre_jugador, resultado)
                    Repositorios.partida1 = partida1.__dict__
                    if resultado == gano:
                        break
                    if letra1 == salida:
                        break
                print('Resultado Jugador 1', Repositorios.partida1)
                estado1 = False
            while estado2:
                while True:
                    try:
                        jugadador2 = input('Turno del jugador 2, tu nombre?: ')
                        dificultad = int(input('Que dificultad'
                                               ' eliges? (1-10): '))
                        palabra = input('Ingresa la palabra a adivinar: ')
                        tipoPalabra = input('Ingresa el tipo de palabra: ')
                        partida2 = servPart.iniciar_partida(jugadador2,
                                                            dificultad,
                                                            palabra,
                                                            tipoPalabra)
                        break
                    except Exception:
                        print('Dificultad erronea :/')
                print('Llego la hora de adivinar!')
                for _ in range(0, partida2.intentos):
                    letra2 = input('Ingrese letra: ')
                    resultado2 = servPart.intentar_letra(partida2, letra2)
                    print(partida2.palabra_aciertos)
                    print('Te quedan', partida2.intentos, 'intentos')
                    print(partida2.nombre_jugador, resultado2)
                    Repositorios.partida2 = partida2.__dict__
                    if resultado2 == gano:
                        break
                    if letra2 == salida:
                        break
                estado2 = False
                print('Resultado Jugador 2', Repositorios.partida2)
                while estado3:
                    condicion = input('Quieres volver a jugar?(s/n): ')
                    if condicion == 's':
                        self.dos_jugadores()
                    elif condicion == 'n':
                        estado3 = False
                    else:
                        print('Error, entrada incorrecta :/')
        except Exception:
            StopIteration
        return True
