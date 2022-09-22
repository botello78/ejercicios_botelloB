'''
    1.- Desarrollar una clase que permita ingresar tres valores por teclado. 
    Luego mostrar el mayor y el menor. La clase debe de tener los siguientes métodos o funciones:
        • Inicializar
        • CalcularMayor
        • CalcularMenor
    En la función del main se debe de declarar un objeto que va a ejecutar las tres funciones de la clase.
'''

def init():
    x = input("Digite Valor #1: ")
    y = input("Digite Valor #2: ") 
    z = input("Digite Valor #3: ") 
    
    mayor(x,y,z)
    menor(x,y,z)

def mayor(x, y, z):
    print("El numero mayor es: " + str(max(x,y,z)))

def menor(x, y, z):
    print("El numero mayor es: " + str(min(x,y,z)))

class main:
    init()

