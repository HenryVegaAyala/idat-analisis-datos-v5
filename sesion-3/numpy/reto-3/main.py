import numpy as np

# Esto es una variable de lista numerica
ventas_diarias = [1500, 2300, 2100, 2500]

# Conversor a un array
ventas = np.array(ventas_diarias)

sumatoria_total = np.sum(ventas)
promedio = np.mean(ventas)
maximo_valor = np.max(ventas)

print(f"Sumatoria total: {sumatoria_total}")
print(f"Promedio: {promedio}")
print(f"Maximo valor: {maximo_valor}")
