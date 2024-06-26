from arma import Arma

class Personaje:
    
    __nombres_personajes = set()

    def __init__(self, nombre: str, salud: int, descripcion: str, arma: Arma, ataque:int = 15, defensa:int = 5, poder:int = 0) -> None:
        self.__nombre = Personaje.__verificar_nombre(nombre)
        self.__salud = salud
        self.__descripcion = descripcion
        self.__arma = arma
        self.__ataque = ataque
        self.__defensa = defensa
        self.__poder = poder

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @classmethod
    def __verificar_nombre(cls, nombre: str) -> str:
        if nombre in cls.__nombres_personajes:
            raise RuntimeError(f"El personaje '{nombre}' ya existe.")
        cls.__nombres_personajes.add(nombre)
        return nombre

    @property
    def salud(self) -> int:
        return self.__salud

    @salud.setter
    def salud(self, nuevoSalud: int) -> None:
        self.__salud = nuevoSalud
    
    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, nuevoDescripcion: str) -> None:
        self.__descripcion = nuevoDescripcion

    @property
    def ataque(self) -> int:
        return self.__ataque

    @ataque.setter
    def ataque(self, nuevoAtaque: int) -> None:
        self.__ataque = nuevoAtaque

    @property
    def defensa(self) -> int:
        return self.__defensa

    @defensa.setter
    def defensa(self, nuevaDefensa: int) -> None:
        self.__defensa = nuevaDefensa
    
    @property
    def poder(self) -> int:
        return self.__poder

    @poder.setter
    def poder(self, nuevoPoder: int) -> None:
        self.__poder = nuevoPoder

    @property
    def arma(self) -> Arma:
        return self.__arma

    # Verifica si el personaje está muerto.
    def muerto(self) -> bool:
        return self.__salud == 0
    
    # Verifica si el ataque puede ser realizado contra el enemigo.
    def validar_ataque(self, tipo: str, enemigo: 'Personaje') -> bool:
        puede_atacar = False

        if tipo == "basico":
            if self.ataque < enemigo.salud:
                puede_atacar = True
        elif tipo == "especial":
            if self.ataque * 3 < enemigo.salud:
                puede_atacar = True
        elif tipo == "arma":
            if self.ataque * 1.5 < enemigo.salud:
                puede_atacar = True

        # Si el daño del ataque es menor que la salud del enemigo, el ataque puede realizarse.
        if puede_atacar:
            return True
        # Si el daño producido es mayor que la salud del enemigo, significa que ese ataque lo mata.
        else:
            enemigo.salud = 0 
            return False

    def ataque_basico(self, enemigo: 'Personaje') -> str:
        if self.validar_ataque("basico", enemigo):
            daño = self.ataque - enemigo.defensa
            enemigo.salud -= max(0, daño)
            self.poder += 1
            return f"{self.nombre} da un golpe."
        return f"{enemigo.nombre} recibe un golpe y muere."

    def ataque_especial(self, enemigo: 'Personaje') -> str:
        if self.poder >= 5:
            if self.validar_ataque("especial", enemigo):
                daño = self.ataque * 3 - enemigo.defensa
                enemigo.salud -= max(0, daño)
                self.poder -= 5
                return f"{self.nombre} lanza un Ataque Especial."
            else: 
                return f"{enemigo.nombre} recibe un Ataque Especial y muere."
        else:
            return f"{enemigo.nombre} esquiva el ataque."

    def ataque_arma(self, enemigo: 'Personaje') -> str:
        if self.validar_ataque("arma", enemigo):
            daño = self.ataque * 1.5 - enemigo.defensa
            enemigo.salud -= max(0, daño)
            self.poder += 2
            return f"{self.nombre} ataca con su Arma."
        else: 
            return f"{enemigo.nombre} recibe un ataque con Arma y muere."

    def __str__(self) -> str:
        return f"{self.nombre} - ({self.descripcion})"