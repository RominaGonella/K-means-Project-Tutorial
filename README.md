# Resumen del proceso

1. La tarea consiste en crear un cluster de 6 grupos a partir de 3 variables de un dataset, utilizando K-means.
2. El dataset original contiene 20640 alojamientos, y para cada uno se dispone de 9 variables. Para crear el cluster se utilizan solamente las coordenadas (longitud y latitud) y la variable 'MedInc'.
3. Se crea el cluster utilizando la función KMeans de sklearn, con cantidad de clusters igual a 6, como se pide en la letra del ejercicio. Se etiquetan las observaciones en la variable creada 'cluster'.
4. Finalmente, se grafican los datos identificando con distintos colores a los distintos grupos.