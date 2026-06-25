import pandas as pd

df = pd.read_csv("mascotas.csv")

moda = df["categoria"].mode()
promedio = df["precio"].mean()

print(f"La moda de la categoría es: {moda.values[0]}")
print(f"El promedio del precio es: {promedio}")