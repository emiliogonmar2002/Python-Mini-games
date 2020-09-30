#Librerias

import random

#Funciones

def panel(num):

    print("\n  T • I • C •   • T • A • C •   • T • O • E •\n\n")
    print("\t      |       |      ")
    print(f"\t  {num[0]}   |   {num[1]}   |   {num[2]}   ")
    print("\t      |       |      ")
    print("\t¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("\t      |       |      ")
    print(f"\t  {num[3]}   |   {num[4]}   |   {num[5]}   ")
    print("\t      |       |      ")
    print("\t¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("\t      |       |      ")
    print(f"\t  {num[6]}   |   {num[7]}   |   {num[8]}   ")
    print("\t      |       |      \n")

def circulo_numero():
    eleccion_computadora = random.randint(0,8)

    return eleccion_computadora

def ganar(lis0,lis1,lis2,lis3,lis4,lis5,lis6,lis7,lis8,value):
    if lis0=="X" and lis1=="X" and lis2=="X" or lis3=="X" and lis4=="X" and lis5=="X" or lis6=="X" and lis7=="X" and lis8=="X" or lis0=="X" and lis3=="X" and lis6=="X" or lis1=="X" and lis4=="X" and lis7=="X" or lis2=="X" and lis5=="X" and lis8=="X" or lis0=="X" and lis4=="X" and lis8=="X" or lis2=="X" and lis4=="X" and lis6=="X":
        value += 1

    return value


#Variables

lis0 = "0"
lis1 = "1"
lis2 = "2"
lis3 = "3"
lis4 = "4"
lis5 = "5"
lis6 = "6"
lis7 = "7"
lis8 = "8"

value = 0


#Listas

num = [lis0,lis1,lis2,lis3,lis4,lis5,lis6,lis7,lis8]

#Main

panel(num)

while value == 0:
    x = int(input('Ingrese la posición en la que desea colocar su "x": '))

    if x==0:
        lis0 = "X"
    elif x==1:
        lis1 = "X"
    elif x==2:
        lis2 = "X"
    elif x==3:
        lis3 = "X"
    elif x==4:
        lis4 = "X"
    elif x==5:
        lis5 = "X"
    elif x==6:
        lis6 = "X"
    elif x==7:
        lis7 = "X"
    elif x==8:
        lis8 = "X"
    
    num = [lis0,lis1,lis2,lis3,lis4,lis5,lis6,lis7,lis8]

    panel(num)

    eleccion_computadora = circulo_numero()

    computadora = False

    while computadora == False:
        
        eleccion_computadora = circulo_numero()

        if eleccion_computadora==0 and lis0!="X" and lis0!="O":
                lis0 = "O"
                computadora = True

        elif eleccion_computadora==1 and lis1!="X" and lis1!="O":
                lis1 = "O"
                computadora = True
        
        elif eleccion_computadora==2 and lis2!="X" and lis2!="O":
                lis2 = "O"
                computadora = True
        
        elif eleccion_computadora==3 and lis3!="X" and lis3!="O":
                lis3 = "O"
                computadora = True
        
        elif eleccion_computadora==4 and lis4!="X" and lis4!="O":
                lis4 = "O"
                computadora = True
            
        elif eleccion_computadora==5 and lis5!="X" and lis5!="O":
                lis5 = "O"
                computadora = True
        
        elif eleccion_computadora==6 and lis6!="X" and lis6!="O":
                lis6 = "O"
                computadora = True
        
        elif eleccion_computadora==7 and lis7!="X" and lis7!="O":
                lis7 = "O"
                computadora = True
        
        elif eleccion_computadora==8 and lis8!="X" and lis8!="O":
                lis8 = "O"
                computadora = True
        else:
            computadora = False

    num = [lis0,lis1,lis2,lis3,lis4,lis5,lis6,lis7,lis8]
    
    panel(num)
    
    value = ganar(lis0,lis1,lis2,lis3,lis4,lis5,lis6,lis7,lis8,value)

if value == 1:
    print("FELICIDADES HAS GANADO!!")
elif value == 2:
    print("HAS PERDIDO")
