import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar los datos
df = pd.read_csv("marketing.csv")

# seleccionar la columna de interés que es la independiente (X)
x = df[["marketing"]] # Considera que debe ser un Dataframe

# seleccionamos la columna dependiente (y)
y = df["ventas"] # Considera que debe ser una serie

# comenzar a entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x, y) # se encarga de entrenar el modelo con los resultados de X, Y

# Creamos el registro de predicción con el nuevo gasto
nueva_fila_marketing = pd.DataFrame([[6000]], columns=["marketing"])
prediccion = modelo.predict(nueva_fila_marketing)
print(f"La predicción de ventas para un inversión de $6000 en marketing es {prediccion[0]:.2f}")

# Creamos el registro de predicción con el nuevo gasto
nueva_fila_marketing = pd.DataFrame([[9000]], columns=["marketing"])
prediccion = modelo.predict(nueva_fila_marketing)
print(f"La predicción de ventas para un inversión de $9000 en marketing es {prediccion[0]:.2f}")