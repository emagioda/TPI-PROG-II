from jugador import Jugador
from escenario import Escenario
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

    def comenzar_partida(self) -> None:
        luchador1 = self.jugador1.personaje
        luchador2 = self.jugador2.personaje
        lista_luchadores = [luchador1, luchador2]
        juego_posible = True

        print(self)
        for i in range(3, 0, -1):
            print(f"     {i}")
            time.sleep(1.5)
        print("¡¡ FIGHT !!\n")

        while juego_posible:
            atacante = random.choice(lista_luchadores)
            enemigo = luchador2 if atacante == luchador1 else luchador1
             
            if luchador1.salud < 30 or luchador2.salud < 30:
                if self.escenario.trampa_mortal:
                    print(f"{atacante.nombre} lazó a {enemigo.nombre} a la Trampa Mortal")
                    print("TRAMPA MORTAL ACTIVA")
                    self.escenario.activar_trampa(enemigo)

            lista_ataques = [atacante.ataque_basico, atacante.ataque_arma, atacante.ataque_especial]
            ataque_elegido = random.choice(lista_ataques)
            time.sleep(1.5)
            ataque_elegido(enemigo)

            print(f"""
Salud {luchador1.nombre}: {luchador1.salud}%
Salud {luchador2.nombre}: {luchador2.salud}%
""")

            if luchador1.muerto() or luchador2.muerto():
                juego_posible = False
                if luchador1.salud != 0:
                    print(f"{luchador1.nombre} is WIN")
                    self.jugador1.partidas_ganadas += 1
                else:
                    print(f"{luchador2.nombre} is WIN")
                    self.jugador2.partidas_ganadas += 1

        luchador1.salud = 100
        luchador1.poder = 0
        luchador2.salud = 100
        luchador2.poder = 0

    def __str__(self) -> str:
        return f"\nPartida: {self.id_partida} - {self.jugador1.personaje.nombre} VS {self.jugador2.personaje.nombre} en {self.escenario}"
