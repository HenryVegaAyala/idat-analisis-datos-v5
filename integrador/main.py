from datos.cargador import CargadorDatos
from analisis.segmentacion import AnalizadorClusters
from analisis.estadisticas import PruebaHipotesis
from modelos.clustering import SegmentadorProductos
from modelos.clasificador import ClasificadorVentas
from visualizacion.graficos import Graficador


def main():
    print("=" * 55)
    print("  PROPUESTA 2: Segmentacion y Clasificacion de Demanda")
    print("=" * 55)

    # PASO 1: Leer el archivo y preparar los datos
    print("\n>>> PASO 1: Cargando y preparando el dataset...")
    cargador = CargadorDatos("dataset.txt")
    df = cargador.cargar()
    df, mediana_unidades = cargador.agregar_variables(df)
    print(f"  Registros cargados   : {len(df):,}")
    print(f"  Tiendas encontradas  : {df['tienda_id'].nunique()}")
    print(f"  Mediana de unidades  : {mediana_unidades:.0f}  (si supera esto es venta alta)")
    print(f"  Registros venta alta : {df['venta_alta'].sum()} de {len(df)}")

    # PASO 2: Segmentar los productos en 3 grupos usando KMeans
    print("\n>>> PASO 2: Agrupando productos con KMeans (3 grupos)...")
    segmentador = SegmentadorProductos(n_clusters=3)
    df = segmentador.entrenar(df)
    segmentador.mostrar_prediccion(200.0, 50)

    # PASO 3: Analizar las caracteristicas de cada grupo
    analizador = AnalizadorClusters(df)
    analizador.mostrar()

    # PASO 4: Prueba estadistica entre el mejor y peor grupo
    resumen = analizador.resumen_por_cluster()
    cluster_mejor = resumen.loc[resumen["revenue_total"].idxmax(), "cluster"]
    cluster_peor = resumen.loc[resumen["revenue_total"].idxmin(), "cluster"]

    grupo_mejor = df[df["cluster"] == cluster_mejor]["revenue"]
    grupo_peor = df[df["cluster"] == cluster_peor]["revenue"]

    prueba = PruebaHipotesis(grupo_mejor, grupo_peor)
    prueba.mostrar(f"Cluster {cluster_mejor}", f"Cluster {cluster_peor}")

    # PASO 5: Clasificar si un producto tendra venta alta o baja
    print(f"\n>>> PASO 5: Predicciones del Arbol de Decision")
    print(f"  (Umbral de venta alta: mas de {mediana_unidades:.0f} unidades)")
    print("-" * 55)
    clasificador = ClasificadorVentas()
    clasificador.entrenar(df)

    casos = [
        (100.0, 0,  "Precio bajo, sin descuento"),
        (100.0, 20, "Precio bajo, descuento 20%"),
        (250.0, 0,  "Precio medio, sin descuento"),
        (250.0, 15, "Precio medio, descuento 15%"),
        (430.0, 0,  "Precio alto, sin descuento"),
    ]
    for precio, descuento, descripcion in casos:
        clasificador.mostrar_prediccion(precio, descuento, descripcion)
    print("-" * 55)
    print("  Los descuentos ayudan a superar el umbral de venta alta.")

    # PASO 6: Mostrar todos los graficos juntos
    print("\n>>> PASO 6: Generando dashboard de graficos...")
    graficador = Graficador(df)
    graficador.mostrar_dashboard(resumen)


if __name__ == "__main__":
    main()
