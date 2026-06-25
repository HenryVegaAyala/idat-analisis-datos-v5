import pandas as pd
    
df= pd.read_csv("notas.csv")

media= df["notas"].mean()
mediana= df["notas"].median()

print(f"media: {media}")
print(f"mediana: {mediana}")