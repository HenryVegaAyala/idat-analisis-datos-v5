import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("4 gráficos en subplots")

# datafake para ejemplos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# --- Gráfico 1: Línea ---
axs[0, 0].plot(x, y)
axs[0, 0].set_title("grafico de linea")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("y")

plt.grid(True, linestyle="--", alpha=0.5)

# --- Gráfico 2: Baras ---
categorias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
ventas = [150, 200, 180, 220, 170]
axs[0, 1].bar(categorias, ventas, color="orange", edgecolor="black")
axs[0, 1].set_title("Ventas del día")
axs[0, 1].set_xlabel("Día")
axs[0, 1].set_ylabel("Ventas")

plt.grid(True, linestyle="--", alpha=0.5)

plt.show()