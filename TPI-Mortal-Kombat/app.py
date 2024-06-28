from datos import *
import random
import time

# Muestra el menú principal del juego.
def menu() -> str:
    return """
-- MORTAL KOMBAT --
1- Iniciar partida
2- Historial
3- Salir
"""

# Solicita y carga los nombres de los jugadores en la lista de jugadores.
def cargar_nombres() -> None:
    for i in range(2):
        jugador = input(f"Ingrese el nombre del Jugador {i + 1}: ")
        lista_jugadores[i].nombre = jugador

# Permite al jugador seleccionar un luchador de la lista de luchadores.
def elegir_luchador() -> None:
    luchadores_disponibles = luchadores.copy()
    
    for jugador in range(2):
        opcion_valida = False
        while not opcion_valida:
            try:
                print(f"\nLuchadores disponibles:")
                for i, luchador in enumerate(luchadores_disponibles):
                    print(f"{i + 1}- {luchador}")
                
                indice = int(input(f"{lista_jugadores[jugador].nombre}, seleccione un luchador: "))
                
                if 1 <= indice <= len(luchadores_disponibles):
                    luchador_elegido = luchadores_disponibles[indice - 1]
                    lista_jugadores[jugador].personaje = luchador_elegido
                    print(f"{lista_jugadores[jugador].nombre} eligió a {luchador_elegido.nombre}")
                    
                    # Remueve el luchador elegido de los disponibles
                    luchadores_disponibles.pop(indice - 1)
                    
                    opcion_valida = True
                else:
                    print("Luchador inexistente. Intente de nuevo.")
            except ValueError:
                print("Ingrese un número válido. Intente de nuevo.")

# Inicia una nueva partida entre los dos jugadores.
def iniciar_partida() -> None:
    elegir_luchador()

    # Se crea una partida
    partida = Partida(lista_jugadores[0], lista_jugadores[1], random.choice(escenarios)) 

    luchador1 = partida.jugador1.personaje
    luchador2 = partida.jugador2.personaje
    lista_luchadores = [luchador1, luchador2]
    juego_posible = True

    print(partida)
    for i in range(3, 0, -1):
        print(f"     {i}")
        time.sleep(1.5)
    print("¡¡ FIGHT !!\n")

    while juego_posible:
        atacante = random.choice(lista_luchadores)
        enemigo = luchador2 if atacante == luchador1 else luchador1
        
        if partida.escenario.trampa_mortal:
            if luchador1.salud < 30 or luchador2.salud < 30:
                print(f"{atacante.nombre} lazó a {enemigo.nombre} a la Trampa Mortal")
                print("TRAMPA MORTAL ACTIVA")
                partida.escenario.activar_trampa(enemigo)
            else:
                print(partida.elegir_ataque(atacante, enemigo))
        else:
            print(partida.elegir_ataque(atacante, enemigo))

        print(f"""
Salud {luchador1.nombre}: {luchador1.salud}%
Salud {luchador2.nombre}: {luchador2.salud}%
""")
        
        if partida.fin_partida():
            juego_posible = False
            if luchador1.salud != 0:
                print(f"{luchador1.nombre} WINS")
                partida.jugador1.partidas_ganadas += 1
            else:
                print(f"{luchador2.nombre} WINS")
                partida.jugador2.partidas_ganadas += 1
        
    partida.reiniciar_personajes()

def mostrar_historial(lista_jugadores:list) -> str:
    print("\nHistorial")
    for i, jugador in enumerate(lista_jugadores, 1):
        print(f"{i} - {lista_jugadores[i-1].nombre} - {jugador}")

def programa_principal() -> None:
    cargar_nombres()
    opcion_valida = False

    while not opcion_valida:
        try:
            print(menu())
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 3:
                if opcion == 1:
                    iniciar_partida()
                elif opcion == 2:
                    mostrar_historial(lista_jugadores)
                elif opcion == 3:
                    print("¡Adios!")
                    opcion_valida = True
            else:
                print("Opción inexistente. Intente de nuevo.")
        except ValueError:
            print("Ingrese un número válido. Intente de nuevo.")

programa_principal()