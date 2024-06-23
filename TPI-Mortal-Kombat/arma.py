class Arma:
    def __init__(self, nombre: str, tipo: str) -> None:
        self.__nombre = nombre
        self.__tipo = tipo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevoNombre: str) -> None:
        self.__nombre = nuevoNombre

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevotipo: str) -> None:
        self.__tipo = nuevotipo
