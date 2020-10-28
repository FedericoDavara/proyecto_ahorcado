from repositorios import Repositorios
from partida import Partida
from random import randint
import random

class ServicesPartidas:

    def get_palabrasList(self):
        return Repositorios.palabrasList

    def add_partida(self, palabra, tipo_palabra,intentos, nombre_jugador, palabra_aciertos):
        lastKey = -1
        for key in Repositorios.partidasList:
            lastKey = key
        posicion= int(lastKey) + 1
        Repositorios.partidasList[posicion] = {'palabra': palabra, 'tipo_palabra': tipo_palabra,'intentos': intentos,'nombre_jugador':nombre_jugador,'palabra_aciertos':palabra_aciertos}    

    def get_random_palabra (self):
        numeroRandom = randint(0,3)
        return Repositorios.palabrasList[numeroRandom]


    def intentar_letra(self, partida, letra):
        letra = letra.upper()
        tamaño = len(partida.palabra)
        contador = 0
        print ("Su palabra tiene '{}' letras".format(tamaño))
        while partida.intentos > 0:
            partida.intentos -= 1
            for i in range (tamaño):
                if letra in partida.palabra[i]:
                    partida.aciertos[i]=letra
                    if partida.aciertos == partida.palabra:
                        return 'Gano'
                if partida.intentos==0:
                    return 'Perdio'
            
                if Partida.aciertos != Partida.palabra:
                    return 'Continua'

    def iniciar_partida (self, nombre, intentos,
                        palabra, tipo_de_palabra):
        if intentos < 1 or intentos > 10:
            raise ValueError('Intentos erroneos')
        if palabra and tipo_de_palabra != '':
            intentosSet = intentos*len(palabra)
            return Partida(palabra, tipo_de_palabra, intentosSet,
                           nombre)
        if palabra or tipo_de_palabra == '':
           
            stringRandom = self.get_random_palabra()
            intentosRandom = intentos*len(stringRandom['palabra'])
            return Partida(stringRandom['palabra'],
                           stringRandom['tipo_palabra'],
                           intentosRandom, nombre)

