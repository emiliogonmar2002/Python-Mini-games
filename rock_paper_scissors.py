#Piedra Papel o Tijera
#Emilio González Martínez

#Librerías
import random

#Funciones
def eleccion(numero):
    if numero == 1:
        play = "piedra"
    elif numero == 2:
        play = "papel"
    elif numero == 3:
        play = "tijera"

    return play

def jugada():
    numero = random.randint(1,3)
    eleccion_variable = eleccion(numero)

    return eleccion_variable

def win(usuario,computadora):
    if (usuario == "piedra" and computadora == "tijera") or (usuario == "tijera" and computadora == "papel") or (usuario == "papel" and computadora == "piedra"):
        print(f"\nElección Usuario: {usuario} --- Elección Computadora: {computadora}")
        print("\nG A N A S T E\n")
    elif (computadora == "piedra" and usuario == "tijera") or (computadora == "tijera" and usuario == "papel") or (computadora == "papel" and usuario == "piedra"):
        print(f"\nElección Usuario: {usuario} --- Elección Computadora: {computadora}")
        print("\nP E R D I S T E\n")

#Main

print("Ingrese el número correspondiente:\n\
    \n\t1. Piedra\
    \n\t2. Papel\
    \n\t3. Tijera\n")

usuario = int(input("Elección: "))
usuario = eleccion(usuario)
computadora = jugada()

win(usuario,computadora)



