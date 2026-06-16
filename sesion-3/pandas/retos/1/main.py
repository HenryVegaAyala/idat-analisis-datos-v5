import pandas as pd

df = pd.read_csv("ventas_enero_csv.csv")

filtrado_ventas = df["precio_unitario"] > 1000

resultado = df[filtrado_ventas]

print(resultado)