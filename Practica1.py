import time
import os

condiciones=[3,0,1]

def discos():
    os.system("cls")
    condiciones[0] = int(input("Ingrese el número de discos: "))

def tiempo():
    os.system("cls")
    condiciones[1] = int(input("Ingrese el tiempo entre movimientos: "))

def imprimir_movimiento(partida,llegada,paso):
    time.sleep(condiciones[1])
    print(paso,". Mover de la torre",partida," a la torre",llegada)

#Utilizando el código visto en la clase número 15
def Hanoi(n,partida,pivote,llegada):
    if n == 1:
        imprimir_movimiento(partida,llegada,condiciones[2])
        condiciones[2] += 1
    else:
        Hanoi(n-1,partida,llegada,pivote)
        Hanoi(1,partida,pivote,llegada)
        Hanoi(n-1,pivote,partida,llegada)

def menu():
    os.system("cls")
    print("MENU PRINCIPAL\n 1. Cambiar el número de discos \n 2. Cambiar el tiempo entre movimientos \n 3. Iniciar la simulación \n 4. Salir")

while True:
    menu()
    opcionMenu = input("Seleccione una opción: ")
    if opcionMenu=="1":
        discos()
    elif opcionMenu=="2":
        tiempo()
    elif opcionMenu=="3":
        os.system("cls")
        Hanoi(condiciones[0], "A", "B", "C")
        condiciones[2]=1
        opcionMenu2 = input("¿Desea regresar al menú principal? [1] Si [2] No \nSeleccione una opción: ")
        if opcionMenu2=="2":
            break
    elif opcionMenu=="4":
        break
    else:
        print ("")
        input("No has ingresado ninguna opción correcta, pulsa cualquier tecla para regresar ")
