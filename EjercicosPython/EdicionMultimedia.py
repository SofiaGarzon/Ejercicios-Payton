"""Ejercicio 2: Desarrolla un sistema de edición multimedia donde los elementos puedan ser renderizados,
almacenados y editados. Algunos elementos combinarán varias de estas funcionalidades.
Define las interfaces Renderizable y Editable. Crea las clases base Almacenable y Procesable. Implementa
la clase Video que herede de Almacenable y Procesable, e implemente Renderizable y Editable. Implementa
la clase Imagen que herede de Almacenable y Renderizable, pero no sea editable. Crea una función que
procese una lista de elementos multimedia llamando a sus métodos según sus capacidades.
Conceptos aplicados: Herencia múltiple, Interfaces, Composición"""

from abc import ABC, abstractmethod 

class Almacenable(ABC):
    def __init__(self):
         
    @abstractmethod
    def renderizable(self):
        pass

class Procesable:
    def __init__(self):
        print("")
    
    def editable(self):
        return print(f"El archivo editado:")
    
class Video(Almacenable, Procesable):
    
    def renderizable(self):
        print(f"Es renderizable")
        
    def editable(self):
        print(f"El archivo editado:")
        
class Imagen(Almacenable, Procesable):
    
    def renderizable(self):
        print(f"Es renderizable")
        
class EdicionMultimedia():
    def __init__(self):
        print("")
        
video = Video()
imagen = Imagen()
        
        
    
    
        