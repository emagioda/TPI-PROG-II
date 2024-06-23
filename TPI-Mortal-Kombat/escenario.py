from personaje import Personaje

class Escenario:
    def __init__(self, nombre: str, fondo: str, trampa_mortal:bool = False) -> None:
        self.__nombre = nombre
        self.__fondo = fondo
        self.__trampa_mortal = trampa_mortal

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevoNombre: str) -> None:
        self.__nombre = nuevoNombre

    @property
    def fondo(self) -> str:
        return self.__fondo

    @fondo.setter
    def fondo(self, nuevoFondo: str) -> None:
        self.__fondo = nuevoFondo

    @property
    def trampa_mortal(self) -> str:
        return self.__trampa_mortal
                      
    # Activa la trampa mortal que reduce la salud del enemigo a 0.
    def activar_trampa(self, enemigo: Personaje) -> None:
        enemigo.salud = 0

    def __str__(self) -> str:
        return f"{self.nombre}"
