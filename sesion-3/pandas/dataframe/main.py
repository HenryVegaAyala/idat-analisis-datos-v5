import pandas as pd

ventas = {
    "nombre": ["Pepito", "Juan"],
    "edades": [25, 30],
    "distrito": ["Surco", "Miraflores"],
}

df = pd.DataFrame(ventas)

print(df)