#Ejemplo 1: Crear una clase con atributos, metodos y generar objetos de esa clase y mostrsr sus detalles


class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def mostrar(self, numero, valor = 0):
        print(f"numero: {numero} valor: {valor} Nombre es: {self.nombre}, La edad es: {self.edad},, el genero es: {self.genero}")
        
#Crear una instancia de esa clase Persona, un objeto
persona1 = Persona("Maria Perez", 35, "Femenino")
persona2 = Persona("Maria Perez", 35, "Femenino")
persona3 = Persona("Maria Perez", 35, "Femenino")

persona1.mostrar(7, 1)
persona2.mostrar(2)
persona3.mostrar(3)