import pandas as pd

df = pd.read_csv("../../dataset.txt")

# filtros
filtro_sucursal = df["Store ID"] == 8091
filtro_precio_total = df["Total Price"] > 100

resultado = df[filtro_sucursal & filtro_precio_total]

orden = resultado.sort_values("Base Price", ascending=False)

print(orden)