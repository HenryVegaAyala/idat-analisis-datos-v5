import pandas as pd

df = pd.read_csv("ventas_enero.csv")

# Crear una nueva columna
df["precio_total"] = df["precio_unitario"] * df["cantidad"]

# Ordenamiento en descendente
df_ordenado = df.sort_values("precio_total", ascending=False)

print(df_ordenado)