import pandas as pd
from sklearn.tree import DecisionTreeClassifier


class ClasificadorVentas:
    """Aprende que combinacion de precio y descuento lleva a venta alta o baja."""

    def __init__(self):
        self.modelo = DecisionTreeClassifier(max_depth=4, random_state=42)

    def entrenar(self, df):
        x = df[["precio_venta", "descuento_pct"]]
        y = df["venta_alta"]
        self.modelo.fit(x, y)

    def predecir(self, precio, descuento):
        entrada = pd.DataFrame([[precio, descuento]], columns=["precio_venta", "descuento_pct"])
        return self.modelo.predict(entrada)[0]

    def mostrar_prediccion(self, precio, descuento, descripcion):
        resultado = self.predecir(precio, descuento)
        etiqueta = "VENTA ALTA" if resultado == 1 else "VENTA BAJA"
        print(f"  {descripcion:<35} -->  {etiqueta}")
