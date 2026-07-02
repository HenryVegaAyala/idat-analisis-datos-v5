import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("dato_credito.csv")

x = df[["ingreso", "morosidad"]]
y = df["aprobado"]

modelo = DecisionTreeClassifier()
modelo.fit(x, y)

prediccion_credito = pd.DataFrame([[2800, 0]], columns=["ingreso", "morosidad"])
resultado = modelo.predict(prediccion_credito)

if resultado == 1:
    print("El crédito fue aprobado.")
else:
    print("El crédito fue rechazado.")
