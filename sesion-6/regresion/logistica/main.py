import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("fuga_clientes.csv")

x = df[["antiguedad", "cuota_mensual"]] # Causa o variable x
y = df["fuga"] # Efecto o variable y

modelo = LogisticRegression()
modelo.fit(x, y)

prediccion_fuga = pd.DataFrame([[3, 50]], columns=["antiguedad", "cuota_mensual"])

resultado = modelo.predict(prediccion_fuga)

if resultado[0] == 1:
    print("El cliente se va a ir.")
else:
    print("El cliente no se va a ir.")