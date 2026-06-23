import pandas as pd

facturacion = pd.read_csv("facturacion.csv")
cliente = pd.read_csv("clientes.csv")

consolidado = pd.merge(facturacion, cliente, on="id_cliente", how="left")

agrupador = consolidado.groupby(["nombre", "pais"]).sum()["monto_total"]

# agrupador