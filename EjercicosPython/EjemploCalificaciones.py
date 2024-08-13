"""Implementa un sistema que lea las calificaciones de los estudiantes de un curso y determine la
calificación promedio, la calificación más alta y la más baja. El usuario debe ingresar el número de
estudiantes y luego la calificación de cada uno. Solicitar al usuario el número de estudiantes.
Utilizar bucles y estructuras condicionales para procesar y comparar las calificaciones. Calcular y
mostrar la calificación promedio, la máxima y la mínima. Mínimo 6 ingresos."""

#Funcion que calcula la sumatoria de las notas de los estudiantes 
def sumatoria_calificaciones(calificaciones):
    sumatoria = 0

    #Recoje todas las calificaciones y calcula su sumatoria
    for i in range(len(calificaciones)):
        sumatoria += calificaciones[i]

    return sumatoria

#Calcula el promedio de las notas
def promedio_calificaciones(sumatoria, estudiantes):
    return sumatoria / estudiantes

#Funcion que captura las calificaciones dependiendo del total de estudiantes ingresados
def num_estudiantes(estudiantes):
    #Array que va a guardar las calificaciones ingresadas
    calificaciones = []
    
    #Se captura cada una de las calificaciones de los estudiantes
    for i in range(estudiantes):
        nota_individual = float(input(f"Digite la calificacion del estudiante {i + 1}: "))
        #Se guarda el valor de la nota en el array
        calificaciones.append(nota_individual)
        
    sumatoria_total = sumatoria_calificaciones(calificaciones)
    
    promedio = promedio_calificaciones(sumatoria_total, estudiantes)
    print(f"El promedio de las notas de los estudiantes del curso es: {promedio}")
    
    #La funcion sort organiza un array de menor a mayor, quedando la calificacion mayor en la ultima posicion del array
    calificaciones.sort()
    
    #Se obtiene la calificacion mayor que esta en la ultima posicion del array
    calificacion_mayor = calificaciones[len(calificaciones) - 1]
    print(f"La calificacion mas alta fue: {calificacion_mayor}")
    
    calificacion_menor = calificaciones[0]
    print(f"La calificacion mas baja fue: {calificacion_menor}")
    
    
       
#Funcion principal del programa
def main():
    #Ciclo infinito que solo se rompe cuando el valor ingresado es valido
    while True: 
        estudiantes = int(input("Digite el numero de estudiantes: "))
        
        if estudiantes >= 6:
            #Se llama la funcion que calcula el total de calificaciones ingresadas
            num_estudiantes(estudiantes)
            break
        else:
            print("Debe recibir la nota de minimo 6 estudiantes")
    

main()