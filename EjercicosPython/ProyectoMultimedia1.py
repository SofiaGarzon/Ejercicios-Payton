"""Ejercicio 1: Desarrolla un sistema para gestionar proyectos multimedia que contengan elementos como
videos, audios e imágenes. Estos elementos pueden existir independientemente o formar parte de un
proyecto.

Crea una clase abstracta ElementoMultimedia con métodos reproducir y obtener_info. Implementa las
clases Video, Audio e Imagen que hereden de ElementoMultimedia. Diseña una clase ProyectoMultimedia
que contenga una lista de ElementoMultimedia y permita agregar elementos, reproducirlos y obtener un
resumen del proyecto.
Conceptos aplicados: Composición, Agregación, Clases abstractas"""


from abc import ABC, abstractmethod 

class ElementoMultimedia(ABC):
    def __init__(self, nombre, descripcion, ID):
        self.nombre = nombre
        self.ID = ID
        self.descripcion = descripcion
    
    @abstractmethod
    def reproducir(self):
        pass

    def obtener_info(self):
        return f"Nombre del archivo: {self.nombre}, {self.descripcion}, {self.ID}"


class Imagen(ElementoMultimedia):
    def __init__(self, nombre, descripcion, ID):
         super(). __init__(nombre, descripcion, ID)
         

    def reproducir(self):
        #return self.calcular_salario_anual() 
        return "La imagen no se puede reproducir"
    
    
         
class Video(ElementoMultimedia):
    def __init__(self, nombre, descripcion, ID):
        super(). __init__(nombre, descripcion, ID)
        self.en_ejecucion = False
        
        
    def reproducir(self):
        #return self.calcular_salario_anual()
        mensaje = ""
        if self.en_ejecucion == True:
            self.en_ejecucion = False
            mensaje = "El video se ha detenido"
        else:
            self.en_ejecucion = True
            mensaje = "El video se esta reproducindo"
            
        return mensaje        
        
        
class Audio(ElementoMultimedia):
    def __init__(self, nombre, descripcion, ID):
        super(). __init__(nombre, descripcion, ID)
        self.en_ejecucion = False
        
    def reproducir(self):
        #return self.calcular_salario_anual() 
        mensaje = ""
        if self.en_ejecucion == True:
            self.en_ejecucion = False
            mensaje = "El Audio se ha detenido"
        else:
            self.en_ejecucion = True
            mensaje = "El Audio se esta reproducindo"
            
        return mensaje        
        

class ProyectoMultimedia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
        
    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)
        
    def reproducir_elemento(self, index):
        return self.elementos[index].reproducir()
     
    def reproducir_elementos(self):
        print(f"Se han reproducido los elementos del proyecto: {self.nombre}")
        for i in range(len(self.elementos)):
            print(self.elementos[i].reproducir())
            
    def resumen_proyecto(self):
        total_elementos = len(self.elementos)
        print(f"{self.nombre} tiene un total de: {total_elementos} elementos")
        
        for i in range(len(self.elementos)):
            print(f"{i+1}: {self.elementos[i].obtener_info()}")
    

    

video1 = Video("introduccion", "enseña como escribir codigo", 1234)
video2 = Video("noticias", "noticias del dia", 4321)
video3 = Video("pelicula", "muestra la pelicula El Principito", 2431)
imagen = Imagen("Fondo", "Imagen usada para portada", 567)
audio = Audio("musica", "himno nacional", 876)


proyecto = ProyectoMultimedia("Proyecto Multimedia")
proyecto.agregar_elemento(video1)
proyecto.agregar_elemento(imagen)
proyecto.agregar_elemento(audio)
proyecto.agregar_elemento(video2)
proyecto.agregar_elemento(video3)

proyecto.resumen_proyecto()


#print(proyecto.reproducir_elemento(0))
#print(proyecto.reproducir_elemento(1))
#print(proyecto.reproducir_elemento(2))

proyecto.reproducir_elementos()

#estado_video = video.reproducir()
#print(estado_video)


#estado_video = video.reproducir()
#print(estado_video)

#estado_audio = audio.reproducir()
#print(estado_audio)


#estado_audio = audio.reproducir()
#print(estado_audio)


#print(video.reproducir(), imagen.reproducir(), audio.reproducir())
#print(video.obtener_info(), imagen.obtener_info(), audio.obtener_info())