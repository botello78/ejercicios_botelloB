'''
    2.- Desarrollar un programa que permita ingresar los lados de un triángulo e implemente los siguientes métodos:
        • Inicializar los atributos
        • Imprimir el valor del lado mayor
        • Un método para mostrar un mensaje si es equilátero o no.
    En la función del main se debe de declarar un objeto que va a ejecutar las tres funciones de la clase.
'''

def init():
    lado1 = input("Digite lado #1: ")
    lado2 = input("Digite lado #2: ") 
    lado3 = input("Digite lado #3: ") 
    
    lado_mayor(lado1,lado2,lado3)
    equilatero(lado1,lado2,lado3)

def lado_mayor(lado1, lado2, lado3):
    print("El valor del lado mayor es: " + str(max(lado1,lado2,lado3)))

def equilatero(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero")
    else: 
        print("El triángulo no es equilátero")

class main:
    init()
