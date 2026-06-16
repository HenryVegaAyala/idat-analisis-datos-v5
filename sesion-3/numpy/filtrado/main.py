import numpy as np

edades = [15, 18, 20, 30, 50, 10]
edades_array = np.array(edades)

# condición para filtrar las edades mayores o iguales a 18
es_mayor = edades_array >= 18
print(f"Condición de filtrado: {es_mayor}")

# Aplicando el filtrado
resultado = edades_array[es_mayor]

print(f"Resultado: {resultado}")