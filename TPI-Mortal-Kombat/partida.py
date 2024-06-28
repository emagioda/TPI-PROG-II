from jugador import Jugador
from escenario import Escenario
from personaje import Personaje
import random
import time

class Partida:
    
    __id_partida = 0
    
    def __init__(self, jugador1: Jugador, jugador2: Jugador, escenario: Escenario) -> None:
        self.__jugador1 = jugador1
        self.__jugador2 = jugador2
        self.__escenario = escenario
        self.__id_partida = Partida.__aumentar_id()

    @property
    def jugador1(self) -> Jugador:
        return self.__jugador1

    @jugador1.setter
    def jugador1(self, nuevo_jugador1: Jugador) -> None:
        self.__jugador1 = nuevo_jugador1

    @property
    def jugador2(self) -> Jugador:
        return self.__jugador2

    @jugador2.setter
    def jugador2(self, nuevo_jugador2: Jugador) -> None:
        self.__jugador2 = nuevo_jugador2

    @property
    def escenario(self) -> Escenario:
        return self.__escenario

    @escenario.setter
    def escenario(self, nuevo_escenario: Escenario) -> None:
        self.__escenario = nuevo_escenario

    @property
    def id_partida(self) -> int:
        return self.__id_partida

    @classmethod
    def __aumentar_id(cls) -> int:
        cls.__id_partida += 1
        return cls.__id_partida

    def elegir_ataque(self, atacante:Personaje, enemigo:Personaje) -> str:
        lista_ataques = [atacante.ataque_basico, atacante.ataque_arma, atacante.ataque_especial]
        ataque_elegido = random.choice(lista_ataques)
        time.sleep(1.5)
        return ataque_elegido(enemigo)
       
    def reiniciar_personajes(self) -> None:
        self.jugador1.personaje.salud = 100
        self.jugador2.personaje.salud = 100

        self.jugador1.personaje.poder = 0
        self.jugador2.personaje.poder = 0

    def fin_partida(self) -> bool:
        luchador1 = self.jugador1.personaje
        luchador2 = self.jugador2.personaje

        return luchador1.muerto() or luchador2.muerto()

    def __str__(self) -> str:
        return f"\nPartida: {self.id_partida} - {self.jugador1.personaje.nombre} VS {self.jugador2.personaje.nombre} en {self.escenario}"