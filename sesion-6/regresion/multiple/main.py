import pandas as pd
from sklearn.linear_model import LinearRegression

# Carga de datos
df = pd.read_csv("datos_salarios.csv")

# Variable independiente X
x = df[["experiencia", "estudios"]] # Causa o variable X
y = df["salario"] # Efecto o variable Y

modelo = LinearRegression()
modelo.fit(x, y)

prediccion = pd.DataFrame([[4,5]], columns=["experiencia", "estudios"])

resultado_prediccion = modelo.predict(prediccion)
print(f"salario sugerido: {resultado_prediccion[0]:.2f}")