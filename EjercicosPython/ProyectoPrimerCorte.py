import cv2
import numpy as np
import matplotlib.pyplot as plt

ruta_imagen = "Imagen/flores.jpg"

def extraer_y_distribuir_colores(ruta_imagen):

    #Leer la imagen.
    img = cv2.imread(ruta_imagen)

    #Separar los canales.
    b, g, r = cv2.split(img)

    #Crear arrays para contar la frecuencia de cada nivel de gris.
    hist_r = np.zeros(256, dtype=int)
    hist_g = np.zeros(256, dtype=int)
    hist_b = np.zeros(256, dtype=int)

    #Contar la frecuencia de cada nivel de gris en cada canal.
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            hist_r[r[i, j]] += 1
            hist_g[g[i, j]] += 1
            hist_b[b[i, j]] += 1

    return hist_r, hist_g, hist_b

distribucion_r, distribucion_g, distribucion_b = extraer_y_distribuir_colores(ruta_imagen)

#Ejemplo de prueba
print("Distribución de los primeros 10 niveles de gris del canal Rojo:")
print(distribucion_r[:10])

print("Distribución de los primeros 10 niveles de gris del canal Verde:")
print(distribucion_g[:10])

print("Distribución de los primeros 10 niveles de gris del canal Azúl:")
print(distribucion_b[:10])

#Gráfica
fig, axs = plt.subplots(3, 1, figsize=(10, 10))
axs[0].plot(distribucion_r, color='red')
axs[0].set_title('Distribución del canal Rojo')
axs[1].plot(distribucion_g, color='green')
axs[1].set_title('Distribución del canal Verde')
axs[2].plot(distribucion_b, color='blue')
axs[2].set_title('Distribución del canal Azul')

plt.show()