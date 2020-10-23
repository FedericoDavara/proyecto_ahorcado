class Partida():
    def __init__ (self, nombre_jugador = '', dificultad = 0, palabra = '', tipo_palabra = '', aciertos = []):
        self.palabra = palabra
        self.tipo_palabra = tipo_palabra
        self.dificultad = dificultad
        self.nombre_jugador = nombre_jugador
        self.aciertos = aciertos 

    # getting
    @property
    def palabra(self):
        return self._palabra

    # setting
    @palabra.setter
    def palabra(self, palabra):
        self._palabra = palabra

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    # setting
    @tipo_palabra.setter
    def tipo_palabra(self, tipo_palabra):
        self._tipo_palabra = tipo_palabra

    @property
    def dificultad(self):
        return self._dificultad

    # setting
    @dificultad.setter
    def dificultad(self, dificultad):
        self._dificultad = dificultad

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    # setting
    @nombre_jugador.setter
    def nombre_jugador(self, nombre_jugador):
        self._nombre_jugador = nombre_jugador

    @property
    def aciertos(self):
        return self._aciertos

    # setting
    @aciertos.setter
    def aciertos(self, aciertos):
        self._aciertos = aciertos