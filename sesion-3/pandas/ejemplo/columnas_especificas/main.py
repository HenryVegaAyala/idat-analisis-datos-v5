import pandas as pd

df = pd.read_csv("../../dataset.txt")

print(df[["ID", "Store ID"]])