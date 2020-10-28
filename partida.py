class Partida():
    def __init__ (self, palabra=None, tipo_palabra=None, intentos=0,
                 nombre_jugador=None, aciertos=''):
        self.palabra = palabra
        self.tipo_palabra = tipo_palabra
        self.intentos = intentos
        self.nombre_jugador = nombre_jugador
        self.aciertos = aciertos 

    # getting
    @property
    def palabra(self):
        return self._palabra
        
    # setting
    @palabra.setter
    def palabra(self, palabra):
        if palabra == '':
            raise ValueError("La palabra no puede estar vacia")
        else:
            palabra = list(palabra.upper())
            self._palabra = palabra 

    @property
    def tipo_palabra(self):
        return self.tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, tipo_palabra):
        if tipo_palabra == '':
            raise ValueError("El tipo de palabra no puede estar vacio")
        else:
            self._tipo_palabra = tipo_palabra.upper()

    @property
    def intentos(self):
        return self.intentos

    # setting
    @intentos.setter
    def intentos(self, intentos):
        if intentos >= 0:
            self._intentos = intentos
        else:
            raise ValueError('Los intentos no pueden ser negativos')

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    # setting
    @nombre_jugador.setter
    def nombre_jugador(self, nombre_jugador):
        if nombre_jugador == '':
            raise ValueError('El nombre del jugador no puede estar vacio')
        else:
            self._nombre_jugador = nombre_jugador.upper()

    @property
    def aciertos(self):
        return self._aciertos

    # setting
    @aciertos.setter
    def aciertos(self, aciertos):
        aciertos = list(aciertos)
        self._aciertos = aciertos
        for _ in range(0, len(self._palabra)):
            self._aciertos.append(None)
        if aciertos[0:] == '':
            aciertos.remove('')