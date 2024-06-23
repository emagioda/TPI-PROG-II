from datos import *

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
                    
                    # Remover el luchador elegido de los disponibles
                    luchadores_disponibles.pop(indice - 1)
                    
                    opcion_valida = True
                else:
                    print("Luchador inexistente. Intente de nuevo.")
            except ValueError:
                print("Ingrese un número válido. Intente de nuevo.")

# Inicia una nueva partida entre los dos jugadores.
def iniciar_partida() -> None:
    elegir_luchador()
    partida = jugar
    partida.comenzar_partida()

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
                    print("\nHistorial")
                    for i, jugador in enumerate(lista_jugadores, 1):
                        print(f"{i} - {lista_jugadores[i-1].nombre} - {jugador}")
                
                elif opcion == 3:
                    print("¡Adios!")
                    opcion_valida = True
            else:
                print("Opción inexistente. Intente de nuevo.")
        except ValueError:
            print("Ingrese un número válido. Intente de nuevo.")

programa_principal()