import numpy as np
import scipy.stats as st


class PruebaHipotesis:
    """Compara dos grupos para saber si su diferencia es real o producto del azar."""

    def __init__(self, grupo_a, grupo_b):
        self.grupo_a = np.array(grupo_a)
        self.grupo_b = np.array(grupo_b)

    def mostrar(self, nombre_a, nombre_b):
        resultado = st.ttest_ind(self.grupo_a, self.grupo_b)
        media_a = np.mean(self.grupo_a)
        media_b = np.mean(self.grupo_b)

        print(f"\n>>> PASO 4: Prueba estadistica — {nombre_a} vs {nombre_b}")
        print("-" * 55)
        print(f"  Revenue promedio {nombre_a}: ${media_a:>10,.0f}")
        print(f"  Revenue promedio {nombre_b}: ${media_b:>10,.0f}")
        print(f"  Valor p                  :  {resultado.pvalue:.4f}")
        print("-" * 55)

        if resultado.pvalue < 0.05:
            print(f"  Resultado: La diferencia ES significativa (p < 0.05).")
            print(f"  Los dos grupos tienen comportamientos de venta distintos.")
            print(f"  No es casualidad: el {nombre_a} rinde mas que el {nombre_b}.")
        else:
            print(f"  Resultado: La diferencia NO es significativa (p >= 0.05).")
            print(f"  Las diferencias observadas pueden deberse al azar.")
