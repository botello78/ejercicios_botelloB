'''
    3.- Desarrollar una clase llamada Alumno y definir como atributos su nombre, edad y calificación. Deberá de tener
    dos constructores, el primero deberá de inicializar el nombre del alumno y el segundo constructor deberá de
    inicializar todos los atributos de la clase. Definir los siguientes métodos:
        • Imprimir los datos ingresados
        • Imprimir un mensaje si es mayor o no de edad (edad >=18)
        • Mandara un mensaje dependiendo de su promedio:
            o Si el promedio es menor a 8 mandar un mensaje de Reprobado.
            o Si el promedio es mayor a 8 pero menor a 10 un mensaje de Aprobado.
            o Si el promedio es igual a 10 un menaje de Excelente.
        • Inicializar la edad y la calificación.
    En la función del main se debe de declarar dos objetos, el primer objeto debe de utilizar el primer constructor y el
    segundo objeto debe de utilizar el segundo constructor. Estos objetos debe de ejecutar las siguientes funciones:
    Imprimir los datos ingresados, Imprimir un mensaje si es mayor o no de edad y Mandar un mensaje dependiendo del
    promedio.
'''
import statistics


class Alumno:
    nombre = ''
    edad = 0
    matematicas = 0.0
    literatura = 0.0
    historia = 0.0
    calificacion = 0.0

    def __init__(self):
        self.nombre = input("Ingrese el Nombre del alumno: ")
        self.edad = int(input("Ingrese la edad del alumno: "))


    def promedio(self):
        self.matematicas = float(input("Ingrese calificación de matemáticas: "))
        self.literatura = float(input("Ingrese calificación de literatura: "))
        self.historia = float(input("Ingrese calificación de historia: "))
        
        data  = [self.matematicas, self.literatura, self.historia]
        self.calificacion = float(statistics.mean(data))

        print(self.nombre +" tiene "+str(self.edad) + " años de edad.")
        if self.edad >= 18:
            print(self.nombre + " es mayor de edad")

        else: 
            print(self.nombre + " es menor de edad")

        if self.calificacion < 8:
            print(self.nombre + " esta reprobado!!! con calificación de " + str(round(self.calificacion, 2)))
        
        if self.calificacion >=8 and self.calificacion < 10 :
            print(self.nombre + " esta aprobado!!! con calificación de " + str(round(self.calificacion, 2)))
        
        elif self.calificacion == 10:
            print(self.nombre + " EXCELENTE ESTA EXENTO!!! con calificación de " + str(round(self.calificacion, 2)))




            
        

#if __name__ == "__main__":
Alumno().promedio()