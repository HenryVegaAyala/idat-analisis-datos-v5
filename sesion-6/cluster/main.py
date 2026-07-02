import pprint

import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("datos_clientes.csv")

x = df[["gasto_anual", "visitas_mes"]]

modelo = KMeans(n_clusters=2)
modelo.fit(x)

df["cluster"] = modelo.labels_

print(df)

agrupador = pd.DataFrame([[500, 10]], columns=["gasto_anual", "visitas_mes"])
grupo_resultado = modelo.predict(agrupador)

print(f"Cliente pertenece al grupo {grupo_resultado[0]}")