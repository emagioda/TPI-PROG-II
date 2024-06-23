# Importacion de clases
from partida import Partida
from jugador import Jugador 
from escenario import Escenario
from personaje import Personaje
from arma import Arma
import random

lista_partidas = []
lista_jugadores = []

# Armas
arma_Scorpion = Arma("Katana", "Espada")
arma_Sub_Zero = Arma("Kori Blade", "Espada de Hielo")
arma_Sonya_Blade = Arma("Kali Sticks", "Bastones de combate")
arma_Raiden = Arma("Staff", "Bastón")
arma_Kitana = Arma("Steel Fans", "Abanicos de acero")

# Luchadores
luchadores = [
    Personaje("Scorpion", 100, "Ninja espectro", arma_Scorpion),
    Personaje("Sub-Zero", 100, "Guerrero de hielo", arma_Sub_Zero),
    Personaje("Sonya Blade", 100, "Agente de las Fuerzas Especiales", arma_Sonya_Blade),
    Personaje("Raiden", 100, "Dios del Trueno y protector de Earthrealm", arma_Raiden),
    Personaje("Kitana", 95, "Princesa Edeniana y guerrera", arma_Kitana)
]

# Lista de escenarios
escenarios = [
    Escenario("Arctika", "Rodeado de nieve que cae.", True),
    Escenario("Kahn's Arena", "Con acido, lava, estacas y triturador como deathtraps."),
    Escenario("Evil Tower", "Dividido en torre clásica y portal, con cambio de escenario."),
    Escenario("Goro's Lair", "Oscuro, con interacción con restos", True),
    Escenario("Hell's Foundry", "Con fundidora de metales y cambio de escenario."),
    Escenario("Lin Kuei Palace", "Restos de miembros del Lin Kuei y Kamidogu."),
    Escenario("Scorpion's Lair", "Escorpiones tallados y antorchas tétricas.", True),
    ]

# Crear jugadores
jugador1 = Jugador(luchadores[1])
jugador2 = Jugador(luchadores[0])

lista_jugadores.append(jugador1)
lista_jugadores.append(jugador2)

# Crear Partida
jugar = Partida(lista_jugadores[0], lista_jugadores[1], random.choice(escenarios))