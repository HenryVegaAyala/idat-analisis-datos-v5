import matplotlib.pyplot as plt

COLORES = ["steelblue", "coral", "mediumseagreen"]


class Graficador:
    """Genera un dashboard con 4 graficos en una sola ventana."""

    def __init__(self, df):
        self.df = df

    def mostrar_dashboard(self, resumen):
        clusters = sorted(self.df["cluster"].unique())

        fig, axs = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle("Dashboard — Segmentacion de Productos y Clasificacion de Demanda",
                     fontsize=13, fontweight="bold")

        # Grafico 1: Scatter coloreado por cluster (muestra la segmentacion)
        for i, cluster in enumerate(clusters):
            subset = self.df[self.df["cluster"] == cluster]
            axs[0, 0].scatter(subset["precio_venta"], subset["unidades_vendidas"],
                              label=f"Cluster {cluster}", color=COLORES[i], alpha=0.6, s=20)
        axs[0, 0].set_title("Grupos de Productos (KMeans)")
        axs[0, 0].set_xlabel("Precio de Venta ($)")
        axs[0, 0].set_ylabel("Unidades Vendidas")
        axs[0, 0].legend(fontsize=8)

        # Grafico 2: Revenue total por cluster
        colores_clusters = [COLORES[i] for i in range(len(resumen))]
        barras = axs[0, 1].bar(resumen["cluster"].astype(str), resumen["revenue_total"],
                               color=colores_clusters)
        axs[0, 1].set_title("Revenue Total por Cluster")
        axs[0, 1].set_xlabel("Cluster")
        axs[0, 1].set_ylabel("Revenue ($)")
        axs[0, 1].bar_label(barras, fmt="$%.0f", fontsize=8, padding=3)

        # Grafico 3: Precio promedio por cluster
        axs[1, 0].bar(resumen["cluster"].astype(str), resumen["precio_promedio"],
                      color=colores_clusters)
        axs[1, 0].set_title("Precio Promedio por Cluster")
        axs[1, 0].set_xlabel("Cluster")
        axs[1, 0].set_ylabel("Precio Promedio ($)")
        for i, (_, fila) in enumerate(resumen.iterrows()):
            axs[1, 0].text(i, fila["precio_promedio"] + 1,
                           f"${fila['precio_promedio']:.0f}", ha="center", fontsize=8)

        # Grafico 4: Unidades promedio por cluster
        axs[1, 1].bar(resumen["cluster"].astype(str), resumen["unidades_promedio"],
                      color=colores_clusters)
        axs[1, 1].set_title("Unidades Vendidas Promedio por Cluster")
        axs[1, 1].set_xlabel("Cluster")
        axs[1, 1].set_ylabel("Unidades Promedio")
        for i, (_, fila) in enumerate(resumen.iterrows()):
            axs[1, 1].text(i, fila["unidades_promedio"] + 0.5,
                           f"{fila['unidades_promedio']:.0f}", ha="center", fontsize=8)

        plt.tight_layout()
        plt.savefig("dashboard_propuesta_2.png", dpi=150)
        plt.show()
        print("\n>>> Grafico guardado como 'dashboard_propuesta_2.png'")
