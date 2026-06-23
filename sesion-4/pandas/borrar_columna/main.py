import pandas as pd

data = pd.read_csv("ventas_enero.csv")

print(data.head())

# Eliminar columna
data.drop("vendedor", inplace=True, axis=1)

print(data.head())

# Eliminar fila
data.drop(0, inplace=True, axis=0)

print(data.head())

# Eliminar multiples columnas
data.drop(["cantidad", "precio_unitario"], inplace=True, axis=1)

print(data.head())