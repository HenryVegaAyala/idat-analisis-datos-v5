import pandas as pd

data = pd.read_csv("facturacion.csv")

data["id_cliente"] = data["id_cliente"].fillna("Desconocido")
print(data)
print("-" * 60)

data_sin_nan = data.dropna()
print(data_sin_nan)

print(data)
print("-" * 60)

data_corregida_de_duplicados = data.drop_duplicates()
print(data_corregida_de_duplicados)