from personaje import Personaje

class Jugador:
    def __init__(self, personaje: Personaje, nombre: str = "Jugador") -> None:
        self.__nombre = nombre
        self.__personaje = personaje
        self.__partidas_ganadas = 0
    
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevoNombre: str) -> None:
        self.__nombre = nuevoNombre
    
    @property
    def personaje(self) -> Personaje:
        return self.__personaje

    @personaje.setter
    def personaje(self, nuevoPersonaje: Personaje) -> None:
        self.__personaje = nuevoPersonaje

    @property
    def partidas_ganadas(self) -> int:
        return self.__partidas_ganadas

    @partidas_ganadas.setter
    def partidas_ganadas(self, nueva_partida_ganada: int) -> None:
        self.__partidas_ganadas = nueva_partida_ganada

    @property
    def nivel(self) -> int:
        return self.partidas_ganadas // 3

    def __str__(self) -> str:
        return f"{self.partidas_ganadas} victorias. - NIVEL: {self.nivel}"
