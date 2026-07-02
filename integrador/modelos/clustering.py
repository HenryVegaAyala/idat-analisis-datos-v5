import pandas as pd
from sklearn.cluster import KMeans


class SegmentadorProductos:
    """Agrupa los registros en clusters segun precio y unidades usando KMeans."""

    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.modelo = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)

    def entrenar(self, df):
        x = df[["precio_venta", "unidades_vendidas"]]
        self.modelo.fit(x)
        df = df.copy()
        df["cluster"] = self.modelo.labels_
        return df

    def predecir(self, precio, unidades):
        entrada = pd.DataFrame([[precio, unidades]], columns=["precio_venta", "unidades_vendidas"])
        return self.modelo.predict(entrada)[0]

    def mostrar_prediccion(self, precio, unidades):
        cluster = self.predecir(precio, unidades)
        print(f"\n  Ejemplo: un producto con precio ${precio:.0f} y {unidades} unidades")
        print(f"  pertenece al Cluster {cluster}.")
