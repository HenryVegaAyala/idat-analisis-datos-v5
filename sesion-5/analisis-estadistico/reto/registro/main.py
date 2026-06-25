import pandas as pd

edades = [10, 12, 10, 11, None, 85, 11]

df = pd.Series(edades)

# Calcular la media de las edades, aplicando el filtro
median = df.median()
print(f"median: {median}")

# reemplazar valores Nan
edades_corregidas = df.fillna(median)

resultado = edades_corregidas[edades_corregidas <= 18]

print(f"Resultado: {resultado}")