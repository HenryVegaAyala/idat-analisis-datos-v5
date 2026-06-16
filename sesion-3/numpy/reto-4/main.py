import numpy as np

temperaturas = [22, 21, 23, 90, 22, 20, 105, 21]
temperaturas = np.array(temperaturas)

error = temperaturas > 50

resultado = temperaturas[error]

cantidad_errores = np.sum(error)

print(f"Valores erróneos: {resultado}")
print(f"cantidad de errores: {len(resultado)}")
