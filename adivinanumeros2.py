#Adivina Números
#Emilio González Martínez
#Este programa adivina el número pensado por el usuario


#Librerías
import random

#Variables
intentos = 0
min_numero = 0
max_numero = 50


#Funciones
def numero_aleatorio(min_numero,max_numero):
    numero = random.randint(min_numero,max_numero)
    return numero

def pregunta_numero(numero):
    print(f"\n¿Tu número es {numero}?\
        \n\t1. Menor\
        \n\t2. Mayor\
        \n\t3. Igual")
    intento = int(input("\n\tRespuesta: "))

    return intento


#Main
print("Para empezar... Necesito conocer un rango:")
min_numero = int(input("Ingrese el numero menor: "))
max_numero = int(input("Ingrese el numero mayor: "))

numero = numero_aleatorio(min_numero,max_numero)
intento = pregunta_numero(numero)


while intento != 3:
    while intento == 2:
        min_numero = numero
        numero = numero_aleatorio(min_numero,max_numero)
        intento = pregunta_numero(numero)

        intentos += 1

    while intento == 1:
        max_numero = numero
        numero = numero_aleatorio(min_numero,max_numero)
        intento = pregunta_numero(numero)

        intentos += 1

print("\n¡ LO SABÍA !")
print(f"Número de intentos: {intentos}")
