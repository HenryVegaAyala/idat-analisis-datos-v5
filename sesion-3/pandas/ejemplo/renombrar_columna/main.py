import pandas as pd

df = pd.read_csv("../../dataset.txt")

# filtros
filtro_sucursal = df["Store ID"] == 8091
filtro_precio_total = df["Total Price"] > 100

resultado = df[filtro_sucursal & filtro_precio_total]

resultado["igv"] = resultado["Total Price"] * 0.18

resultado.rename(columns={"igv": "IGV"}, inplace=True)

print(resultado)
