import pandas as pd

df = pd.read_csv("casas.csv")

cantidad_nullos = df["precios"].isnull().sum()

print(f"cantidad_nullos: {cantidad_nullos}")

describe = df.describe()

print(f"describe: {describe}")
