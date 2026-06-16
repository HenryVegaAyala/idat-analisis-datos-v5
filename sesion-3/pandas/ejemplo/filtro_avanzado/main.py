import pandas as pd

df = pd.read_csv("../../dataset.txt")

# filtros
filtro_sucursal = df["Store ID"] == 8091
filtro_precio_total = df["Total Price"] > 100
filtro_indice = df.index < 10

# aplicar filtro
resultado = df[(filtro_sucursal & filtro_precio_total) & filtro_indice]

print(resultado)
