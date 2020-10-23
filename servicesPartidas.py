from repositorios import Repositorior
from partida import Partida
from random import randint

class ServicesPartidas:

    def get_palabrasList(self):
        return Repositorios.palabrasList

    def add_palabra(palabra, tipo_palabra):
        lastKey = -1
        for key in Repositorios.palabrasList:
            lastKey = key
        palabra_new = int(lastKey) + 1
        Repositorios.palabrasList[palabra_new] = {'palabra': palabra, 'tipo_palabra': tipo_palabra}
    
    def valor_inicial_palabra(palabra):
        while palabra == '':
            palabra = input("Debe ingresar una palabra: ")
        return palabra 

    def valor_inicial_nombre_jugador(nombre_jugador):
        while nombre_jugador == '':
            nombre_jugador = input("Debe ingresar un nombre: ")
        return nombre_jugador 
    
    def valor_inicial_tipo_palabra(tipo_palabra):
        while tipo_palabra == '':
            tipo_palabra = input("Debe ingresar el tipo de palabra: ")
        return tipo_palabra     

    def valor_inicial_dificultad(dificultad):
        while dificultad > 0 && dificultad < 11:
            dificultad = input("Debe ingresar una dificultad del 1 al 10: ")
        return dificultad
    
    def valor_inicial_intentos(dificultad):
        while dificultad > 0 && dificultad < 11:
            dificultad = input("Debe ingresar una dificultad del 1 al 10: ")
        return dificultad

    def get_random_palabra ():
        numeroRandom = randint(0,10)
        return Repositorios.palabrasList[numeroRandom]
    
    def iniciar_partida (nombre_jugador, intentos, palabra, tipo_palabra, aciertos):
        partida = Partida (nombre_jugador, intentos, palabra, tipo_palabra, aciertos)

    def iniciar_partida_palabra_random(nombre_jugador, intentos, aciertos):
        partida = Partida (nombre_jugador, intentos, get_random_palabra['palabra'], get_random_palabra['tipo_palabra'], aciertos)

  