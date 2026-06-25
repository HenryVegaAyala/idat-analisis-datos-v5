import pandas as pd

data = pd.Series([20, 22, 22, 25, 61])

mediana = data.median()
media = data.mean()
moda = data.mode()

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda.values[0]}")