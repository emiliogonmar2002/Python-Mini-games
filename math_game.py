"""
--------------------AUTOR------------------------------
Emilio González Martínez    A01640120
-------------------------------------------------------
"""

"""
*******************************************************
-------------------------Librerías---------------------
*******************************************************
"""

import random

"""
*******************************************************
------------------------Funciones----------------------
*******************************************************
"""
#Esta función nos despliega el ejercicio de suma
def suma():

    print("\n. : S U M A : .\n")

    aciertos = 0                        #Contador de aciertos

    for i in range(5):                  #Ciclo for, para mostrar las operaciones 5 veces 
        num1 = random.randint(1,9)      #Generador de números random de 1 digito
        num2 = random.randint(1,9)

        respuesta = int(input(f"\n{num1} + {num2} = ")) #Entrada de la respuesta del usuario

        if respuesta == num1 + num2:                    #Se compara si su respuesta es correcta
            aciertos += 1                               #Se añade uno al contador

    print(f"\nAciertos: {aciertos}\n")                  #Se muestran los aciertos totales del nivel 1

    if aciertos == 5:                                   #Se avanza de nivel si tiene 5 aciertos en el nivel anterior
        print("---------------------------------------------------------------------\
                \n°\ ,,,,, /°\
                \n .(◔␣◔)\
                \n <( ▓ )> .:FELICIDADES AVANZASTE AL NIVEL DOS:.----------------------\
                \n ...╝╚ ♥\
                \n---------------------------------------------------------------------")
        
        aciertos = 0                                    #Se reinicia el contador de aciertos para volver a contar 5

        for i in range(5):                              #Ciclo para repetir 5 veces las operaciones
            num1 = random.randint(1,9)                  #Generación random de un número de un dígito
            num2 = random.randint(10,99)                #Generación de un número random de dos digitos

            respuesta = int(input(f"\n{num1} + {num2} = ")) #Entrada de la respuesta del usuario

            if respuesta == num1 + num2:                    #Se compara si su respuesta es correcta
                aciertos += 1                               #Se añade uno al contador
        
        print(f"\nAciertos: {aciertos}\n")                  #Se muestran los aciertos totales del nivel 2

        if aciertos == 5:                                   #Si sus aciertos son 5(todos) gana el juego
            print(f'---------------------------------------------------------------------\
            \n......(\_/)\
            \n......( "_")\
            \n..../""""""""""""\======┣▇▇▇▇═─....BIENVENIDO AL SALÓN DE LA FAMA....\
            \n/""""""""""""""""""""\
            \n---------------------------------------------------------------------')

#Esta función nos despliega el ejercicio de resta
def resta():

    print("\n. : R E S T A : .\n")

    num1 = random.randint(10,99) #Mostrará un número random de dos dígitos
    num2 = random.randint(10,99) #Mostrará un número random de dos dígitos

    for i in range(5):    #Ciclo for, para mostrar las operaciones 5 veces

        resultado = int(input(f"{num1} - {num2} = ")) #Entrada de la respuesta del usuario

        while resultado != num1 - num2:               #Mientras el resultado sea diferente a resultado se generará de nuevo la misma operación hasta que este correcta
            resultado = int(input(f"{num1} - {num2} = "))
        
        num1 = random.randint(10,99)                #Se vuelve a generar los números aleatorios
        num2 = random.randint(10,99)
    
    print("\n         \|||/\
    \n         (o o)\
    \n------ooO-(_)-Ooo------\n\
    \n★★★ G A N A S T E ★★★\
    \n★★★★★★★★★★★★★★★★★★★★★★")

#Esta función nos despliega el ejercicio de multiplicación
def multiplicacion():

    print("\n. : M U L T I P L I C A C I O N : .\n")

    aciertos = 10    #Número de aciertos tendra que ser 10

    for i in range(10):    #Ciclo for, para mostrar las operaciones 10 veces
        num1 = random.randint(1,9) #Se desplegaran número random con un solo dígito.
        num2 = random.randint(1,9)

        resultado = int(input(f"\n{num1} x {num2} = "))

        if resultado == num1*num2:     #Evaluará si el numero es correcto, se le mostra un mensaje de correcto
            print("\n✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓\nC O R R E C T O :)\n✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓\n")

        else:                          #De lo contrarío será incorrecto.
            print("\nXXXXXXXXXXXXXXXXXXXXXX\nI N C O R R E C T O :(\nXXXXXXXXXXXXXXXXXXXXXX\n")
            aciertos -= 1
    
    print(f"╔═════════════════════════╗\n  Numero de aciertos: {aciertos}\n╚═════════════════════════╝ \n")

#En esta función se encuentra el diseño del menú principal, así como la entrada de la opción a elegir
def menu():            
    print(" __^__                                      __^__\
            \n( ___ )------------------------------------( ___ )\
            \n | / |                                      | \ |\
            \n | / |   -MATEMÁTICAS JUEGO INTERACTIVO-    | \ |\
            \n |___|                                      |___|\
            \n(_____)------------------------------------(_____)\n\
        \n 1. Suma\
        \n 2. Resta\
        \n 3. Multiplicación\
        \n 4. Salir\
        \n------------.:MENU:.------------")

    menu_opcion = input("\nIngrese la opción deseada: ")

    return menu_opcion

"""
*******************************************************
-------------------PROGRAMA PRINCIPAL------------------
*******************************************************
"""

menu_opcion = menu()
#Se evaluará que opción ingreso el cliente para poder mandarlo a la opción elegida y realizar la operación.
while menu_opcion != "4":         
    if menu_opcion == "1":
        suma()
        menu_opcion = menu()
        
    elif menu_opcion == "2":
        resta()
        menu_opcion = menu()
    
    elif menu_opcion == "3":
        multiplicacion()
        menu_opcion = menu()
    
    else:
        print("\n███▓▒░░.E R R O R.░░▒▓███\n INGRESE UN NÚMERO VÁLIDO")
        menu_opcion = menu()
#Si el usuario da la opción de salir el programa tendrá que slair del while para darle un mesnaje de despedida
print('\t oooO \
\n\t(....)    Oooo\
\n\t...(     (....)\
\n\t._)      )../\
\n\t         (_/ \
\n\n\tGRACIAS POR JUGAR \
\n\n\t¡Vuelve pronto!\n')