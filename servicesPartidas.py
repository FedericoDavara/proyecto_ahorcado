from repositorios import Repositorios
from partida import Partida
from random import randint

class ServicesPartidas:

    def get_palabrasList(self):
        return Repositorios.palabrasList

    def add_partida(self, palabra, tipo_palabra,intentos, nombre_jugador, palabra_aciertos):
        lastKey = -1
        for key in Repositorios.partidasList:
            lastKey = key
        posicion= int(lastKey) + 1
        Repositorios.partidasList[posicion] = {'palabra': palabra, 'tipo_palabra': tipo_palabra,'intentos': intentos,'nombre_jugador':nombre_jugador,'palabra_aciertos':palabra_aciertos}
    
    def valor_inicial_palabra(self):
        palabra = ''
        while palabra == '':
            palabra = input("Debe ingresar una palabra: ")
        return palabra 

    def valor_inicial_nombre_jugador(self):
        nombre_jugador = ''
        while nombre_jugador == '':
            nombre_jugador = input("Debe ingresar un nombre: ")
        return nombre_jugador 
    
    def valor_inicial_tipo_palabra(self):
        tipo_palabra = ''
        while tipo_palabra == '':
            tipo_palabra = input("Debe ingresar el tipo de palabra: ")
        return tipo_palabra     

    #def valor_inicial_dificultad(self, dificultad):
        #while dificultad > 0 & dificultad < 11:
            #dificultad = input("Debe ingresar una dificultad del 1 al 10: ")
        #return dificultad
    
    def valor_inicial_intentos(self, palabra, dificultad):
        intentos = len(palabra)*dificultad
        valor_intentos_mayor(intentos)
        valor_intentos_menor(intentos)
        return intentos

    def valor_intentos_mayor(self, intentos):
        if intentos > 15:
            intentos = 15
        return intentos

    def valor_intentos_menor(self, intentos):
        if intentos < 1:
            intentos = 1
        return intentos

    def get_random_palabra (self):
        numeroRandom = randint(0,10)
        return Repositorios.palabrasList[numeroRandom]

    def result(self):
        return result

    def intentos_final(self,intentos):
        return intentos

    def intentar_letras(self, dificultad, letras, result):
        intentos = valor_inicial_intentos(dificultad,letras)
        tamaño = len(letras)
        print ("Su palabra tiene '{}' letras".format(tamaño))
        while intentos > 0:
            letra = input("Ingrese una letra: ")
            print ('Usted ingreso la letra: ',letra)
            for indice,letra in letras:
                if letras[indice] == letra:
                    result [indice] = letra
                    if letras [indice] == result [indice]:
                        intentos = intentos - 1
                        intentosf = intentos
                        intentos_final(intentosf)
                        intentos = 0
                        estado = 'Ganó'
                        print (estado)
                    elif intentos == 1:
                        intentos = intentos - 1
                        intentos_final(intentos)
                        estado = 'Perdió'
                        print (estado)
                    else:
                        estado = 'Continua'
                        intentos = intentos - 1
                        print (estado)
        return result

    def iniciar_partida (self):
        dificultad = int(input("Ingrese la dificultad del 1 al 10: "))
        palabra =  valor_inicial_palabra()
        nombre = valor_inicial_nombre_jugador()
        tipo_palabra = valor_inicial_tipo_palabra()
        print ("Su tipo de palabra es '{}' ".format(tipo_palabra))
        aciertos =  intentar_letras(dificultad,palabra,result())
        partida = Partida (nombre, dificultad, palabra, tipo_palabra, aciertos)
        add_partida(palabra,tipo_palabra, intentos, nombre, aciertos)

    def iniciar_partida_palabra_random(self):
        dificultad = int(input("Ingrese la dificultad del 1 al 10: "))
        nombre_jugador = valor_inicial_nombre_jugador()
        get_random_palabra = get_random_palabra () 
        palabra = get_random_palabra['palabra']
        tipo_palabra = get_random_palabra['tipo_palabra']
        print ("Su tipo de palabra es '{}' ".format(tipo_palabra))
        aciertos =  intentar_letras(dificultad,palabra,result())
        partida = Partida (nombre_jugador, dificultad, palabra, tipo_palabra, aciertos)
        add_partida(palabra,tipo_palabra, intentos, nombre_jugador, aciertos)