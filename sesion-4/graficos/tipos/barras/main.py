import matplotlib.pyplot as plt

ciudades = ["Lima", "Cusco", "Arequipa"]
ventas = [500, 300, 450]

barras = plt.bar(ciudades, ventas, color=["red", "green", "blue"])

# Títulos y etiquetas
plt.title("Ventas por ciudad", fontsize=16, fontweight="bold")
plt.xlabel("Ciudades")
plt.ylabel("Ventas")

# Agregar valores encima de cada barra
for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + (barra.get_width() / 2),
        altura + 5,
        f"{altura}",
        ha='center',
        fontsize=11,
    )

# Mejora visual
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.show()
