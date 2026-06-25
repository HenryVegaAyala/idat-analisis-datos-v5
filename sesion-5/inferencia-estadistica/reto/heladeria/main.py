import pandas as pd
import numpy as np
import scipy.stats as st

# 1. Leer y cargar datos en memoria
df = pd.read_csv("gastos.csv")
dato_de_gastos = df["gasto"]

# 2. Calcular el intervalo de confianza al 95%
intervalo = st.t.interval(
    confidence=0.95,  # porcentaje de intervalos de confianza
    df=len(dato_de_gastos) - 1, # Ajustes de cantidad de datos
    loc=np.mean(dato_de_gastos),  # media de los datos -> promedio
    scale=st.sem(dato_de_gastos) # error estándar de la media
)

print(f"El cliente en promedio gasta entre S/.{intervalo[0]:.2f} y S/.{intervalo[1]:.2f}")

# Punto medio
promedio = (intervalo[0] + intervalo[1]) / 2
print(f"El promedio de gasto es: S/.{promedio:.2f}")

# Margen de error
print(promedio - intervalo[0])
print(intervalo[1] - promedio)