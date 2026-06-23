import matplotlib.pyplot as plt

edades = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 50]

plt.hist(edades, bins=5, edgecolor="black", color="red")

plt.title("Histograma de edades")
plt.xlabel("Edades")
plt.ylabel("Frecuencia")

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.show()
