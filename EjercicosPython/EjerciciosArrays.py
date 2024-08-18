
import numpy as np

arreglo1 = np.array(
    [
        [10, 20 ,30], 
        [40, 50, 60],
        [70, 80, 90]
    ])

arreglo2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 7, 8]
])

#Acceder usando doble indice
#elemento1 = arreglo2[1][2]
#elemento2 = arreglo2[0, 1]

"""print(arreglo1[1][2])
arreglo1[1][2] = 7
print(arreglo1[1][2])"""
#Seleccionar todas las filas de una columna
#print(arreglo2[:, 0]) # : para postrar todas las filas de una columna



#print("Iterar por elementos")
#for i in arreglo2.flat:
  #  print(i)

#arreglo4 = np.append(arreglo2, arreglo1, axis=0)
#arreglo3 = np.append(arreglo2, [[10], [11], [12], [13]], axis=1)
#print(arreglo4)
#print(arreglo3)


#Arreglo 3D

arreglo3D = np.array(
    [
        [
            [255, 0, 0], 
            [0, 255, 0],
            [0, 0, 255], 
            [255, 255, 0]
        ]
    ]
)


print(f"arreglo 3D: {arreglo3D.shape}")
print(arreglo3D)
print("================================")


#nueva_capa = np.array([[[100], [100]], [[100], [100]]])
nueva_capa = np.array(
    [
        [
            [100, 200, 300],
            [400, 500, 600],
            [100, 200, 300],
            [400, 500, 600]
            
        ]
    ]
)

print(f"nueva capa: {nueva_capa.shape}")
print(nueva_capa)
print("================================")

arreglo3D = np.append(arreglo3D, nueva_capa, axis=2)
print(arreglo3D)
print(f"Shape arreglo 3D axis 2: {arreglo3D.shape}")





#nueva_capa2 = np.array([[[100], [100]], [[100], [100]]])
#arreglo3D = np.append(arreglo3D, nueva_capa, axis=2)



