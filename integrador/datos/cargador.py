import pandas as pd


class CargadorDatos:
    """Lee el archivo CSV y prepara las columnas que vamos a usar."""

    def __init__(self, ruta):
        self.ruta = ruta

    def cargar(self):
        df = pd.read_csv(self.ruta)
        df = df.dropna()
        df.columns = ["id", "tienda_id", "precio_venta", "precio_base", "unidades_vendidas"]
        df["tienda_id"] = df["tienda_id"].astype(str)
        return df

    def agregar_variables(self, df):
        """Crea columnas nuevas para el analisis."""
        df = df.copy()

        # Cuanto dinero genero cada venta
        df["revenue"] = df["precio_venta"] * df["unidades_vendidas"]

        # Que porcentaje de descuento se aplico
        df["descuento_pct"] = ((df["precio_base"] - df["precio_venta"]) / df["precio_base"] * 100).round(2)

        # Verdadero o Falso si hubo descuento
        df["tiene_descuento"] = df["descuento_pct"] > 0

        # Si las unidades vendidas superan la mediana = venta alta (1), sino venta baja (0)
        mediana = df["unidades_vendidas"].median()
        df["venta_alta"] = (df["unidades_vendidas"] > mediana).astype(int)

        return df, mediana
