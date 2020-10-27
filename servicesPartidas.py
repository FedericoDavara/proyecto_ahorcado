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
        intentos = len(palabra)
        intentos = intentos * dificultad
        self.valor_intentos_mayor(intentos)
        self.valor_intentos_menor(intentos)
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
        numeroRandom = randint(0,3)
        return Repositorios.palabrasList[numeroRandom]

    def result(self):
        result = ''
        return result

    def intentar_letras(self, dificultad, letras, result):
        intentos = self.valor_inicial_intentos(letras, dificultad)
        tamaño = len(letras)
        contador = 0
        print ("Su palabra tiene '{}' letras".format(tamaño))
        while intentos >= 0:
            letra = input("Ingrese una letra: ")
            print ('Usted ingreso la letra: ',letra)
            if letra in letras:
                for i in range (tamaño):
                    if letra in letras[i]:
                        result = result + letra
                intentos = intentos - 1
            elif intentos == 1 and letra not in letras:
                result = result + letra
                estado = 'Perdió'
                intentos = -1
                print (estado)
                break
            elif intentos > 1 and letra not in letras:
                result = result + letra
                estado = 'Continua'
                intentos = intentos -1
                print (estado)
            if letra in letras:
                contador = contador + 1
                if contador == len(letras):
                    result = letras
                    intentos = -1
                    estado = 'Ganó'
                    print (estado)
                    break
            print (intentos)
        lista = [result, intentos] 
        return lista

    def iniciar_partida (self):
        dificultad = int(input("Ingrese la dificultad del 1 al 10: "))
        palabra =  self.valor_inicial_palabra()
        longitud = len(palabra)
        nombre = self.valor_inicial_nombre_jugador()
        tipo_palabra = self.valor_inicial_tipo_palabra()
        print ("Su tipo de palabra es '{}' ".format(tipo_palabra))
        aciertos =  self.intentar_letras(dificultad,palabra,self.result())[0]
        intentos = self.intentar_letras(dificultad,palabra,self.result())[1]
        partida = Partida (nombre, dificultad, palabra, tipo_palabra, aciertos)
        self.add_partida(palabra,tipo_palabra, intentos, nombre, aciertos)

    def iniciar_partida_palabra_random(self):
        dificultad = int(input("Ingrese la dificultad del 1 al 10: "))
        nombre_jugador = self.valor_inicial_nombre_jugador()
        get_random_palabra = self.get_random_palabra () 
        palabra = get_random_palabra['palabra']
        tipo_palabra = get_random_palabra['tipo_palabra']
        print ("Su tipo de palabra es '{}' ".format(tipo_palabra))
        aciertos =  self.intentar_letras(dificultad,palabra,self.result())[0]
        intentos = self.intentar_letras(dificultad,palabra,self.result())[1]
        partida = Partida (nombre_jugador, dificultad, palabra, tipo_palabra, aciertos)
        self.add_partida(palabra,tipo_palabra, intentos, nombre_jugador, aciertos)