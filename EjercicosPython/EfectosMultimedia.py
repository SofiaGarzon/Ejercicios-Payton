"""Ejercicio 3: Crea un sistema de efectos multimedia que permita aplicar efectos como filtros de color,
recorte y transiciones a videos e imágenes. Algunos efectos se aplican a todos los tipos de multimedia y
otros son específicos.
Crea una clase abstracta EfectoMultimedia con métodos aplicar y obtener_info. Implementa una interfaz
Aplicable con un método aplicar_efecto. Desarrolla las clases FiltroColor, Recorte y Transicion que hereden
de EfectoMultimedia. Define ElementoConEfectos, que implemente Aplicable y contenga una lista de
EfectoMultimedia. Implementa VideoConEfectos e ImagenConEfectos que hereden de
ElementoConEfectos. Crea un programa que aplique efectos a elementos multimedia y muestre los
resultados.
Conceptos aplicados: Composición, Herencia múltiple, Clases abstractas"""

from abc import ABC, abstractmethod 

class Efecto_multimedia(ABC):
    def __init__(self, video, imagen):
        self.video = video
        self.imagen = imagen
        
    lista_efectos = ["loop", "blanco_negro"]
        
    @abstractmethod
    def aplicar(self):
        pass

    def obtener_info(self):
        return f"Nombre del archivo: {self.video}, {self.imagen}"
    
class Aplicable(ABC):
    @abstractmethod
    def aplicar_efecto(self, efecto):
        pass
    
class FiltroColor(Efecto_multimedia):
    def __init__(self, video, imagen):
         super(). __init__(video, imagen)
         

    def aplicar(self):
        return "La imagen no se puede reproducir"
    
class Recorte(Efecto_multimedia):
    def __init__(self, video, imagen):
         super(). __init__(video, imagen)
         

    def aplicar(self):
        return "La imagen no se puede reproducir"
    
    
class Transicion(Efecto_multimedia):
    def __init__(self, video, imagen):
         super(). __init__(video, imagen)
         

    def aplicar(self):
        return "La imagen no se puede reproducir"
    

class ElementoConEfectos(Aplicable):
    def aplicar_efecto(self):
        return lista_efectos
    

class Video_efectos(ElementoConEfectos):
    
    
class Imagen_efectos(ElementoConEfectos):
    
  
    