""" Desarrolla un programa que calcule el total de ventas de un día, el promedio de ventas y la venta
más alta. El usuario debe ingresar el número de ventas del día y luego el valor de cada venta.
Solicitar al usuario el número total de ventas del día. Calcular y mostrar el total de ventas, el
promedio y la venta más alta. Mínimo 10 entradas."""


#Funcion que calcula el total de las ventas por dia
def sumatoria_ventas(ventas):
    sumatoria = 0

    #Recorrer todas las ventas y calcula su sumatoria
    for i in range(len(ventas)):
        sumatoria += ventas[i]

    return sumatoria

#Calcula el promedio de las ventas
def promedio_ventas(sumatoria, total_ventas):
    return sumatoria / total_ventas

#Funcion que captura las ventas dependiendo del total de ventas ingresadas
def capturar_ventas(total_ventas):
    #Array que va a guardar los precios ingresados
    ventas = []
    
    #Se captura cada una de las ventas
    for i in range(total_ventas):
        valor_venta = int(input(f"Digite el valor para la venta {i + 1}: "))
        #Se guarda el valor de la venta en el array
        ventas.append(valor_venta)
        
    sumatoria_total = sumatoria_ventas(ventas)
    print(f"El total de ventas es: {sumatoria_total}")
    
    promedio = promedio_ventas(sumatoria_total, total_ventas)
    print(f"El promedio de las ventas es: {promedio}")
    
    #La funcion sort organiza un array de menor a mayor, quedando la venta mayor en la ultima posicion del array
    ventas.sort()
    
    #Se obtiene la venta mayor que esta en la ultima posicion del array
    venta_mayor = ventas[len(ventas) - 1]
    print(f"La venta mas alta fue: {venta_mayor}")
    
    
       
#Funcion principal del programa
def main():
    #Ciclo infinito que solo se rompe cuando el valor ingresado es valido
    while True: 
        total_ventas = int(input("Digite el numero de ventas en el día: "))
        
        if total_ventas >= 10:
            #Se llama la funcion que calcula el total de ventas ingresadas
            capturar_ventas(total_ventas)
            break
        else:
            print("El numero de ventas debe ser igual o mayor que 10")
    

main()