class AnalizadorClusters:
    """Analiza las caracteristicas de cada grupo (cluster) encontrado por KMeans."""

    def __init__(self, df):
        self.df = df

    def resumen_por_cluster(self):
        return (
            self.df.groupby("cluster")
            .agg(
                precio_promedio=("precio_venta", "mean"),
                unidades_promedio=("unidades_vendidas", "mean"),
                revenue_total=("revenue", "sum"),
                cantidad=("id", "count"),
            )
            .round(2)
            .reset_index()
        )

    def mostrar(self):
        resumen = self.resumen_por_cluster().sort_values("revenue_total", ascending=False)
        mejor = resumen.iloc[0]
        peor = resumen.iloc[-1]

        print("\n>>> PASO 3: Caracteristicas de cada grupo encontrado")
        print("-" * 60)
        print(f"  {'Grupo':<8} {'Precio Prom.':>14} {'Und. Prom.':>12} {'Revenue Total':>15} {'N':>6}")
        print("-" * 60)
        for _, fila in resumen.iterrows():
            print(
                f"  Cluster {fila['cluster']:<2}  "
                f"${fila['precio_promedio']:>12,.0f}  "
                f"{fila['unidades_promedio']:>10.0f}  "
                f"${fila['revenue_total']:>13,.0f}  "
                f"{fila['cantidad']:>5}"
            )
        print("-" * 60)
        print(f"  Grupo con mas revenue   : Cluster {mejor['cluster']}")
        print(f"    Precio prom. ${mejor['precio_promedio']:,.0f} | {mejor['unidades_promedio']:.0f} unidades prom.")
        print(f"  Grupo con menos revenue : Cluster {peor['cluster']}")
        print(f"    Precio prom. ${peor['precio_promedio']:,.0f} | {peor['unidades_promedio']:.0f} unidades prom.")
        print(f"  Estrategia: replicar las condiciones del Cluster {mejor['cluster']} en los demas grupos.")
