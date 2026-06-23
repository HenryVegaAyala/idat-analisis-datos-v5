import pandas as pd
import glob

# Buscar todos los archivos que tengan .csv automáticamente
buscar_archivos = glob.glob("ventas_*.csv")

# Variable auxiliar para la carga de archios
dataFrames = []

# Leer y unificar todos los archivos csv
for archivo in buscar_archivos:
    df = pd.read_csv(archivo)
    df["archivo"] = archivo
    dataFrames.append(df)

consolidado_anual = pd.concat(dataFrames, ignore_index=True)

consolidado_anual.to_csv("consolidado_anual.csv")

