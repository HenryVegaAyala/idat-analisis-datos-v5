import pandas as pd

enero = pd.read_csv("ventas_enero.csv")
febrero = pd.read_csv("ventas_febrero.csv")

consolidado = pd.concat([enero, febrero])

print(consolidado)