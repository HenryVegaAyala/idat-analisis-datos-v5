import pandas as pd

df = pd.read_csv("../../dataset.txt")

# filtro para obtener solo los registros de Store ID 8091
sucursal = df["Store ID"] == 8091

# filtro aplicado para obtener registros
resultado = df[sucursal]

print(resultado)