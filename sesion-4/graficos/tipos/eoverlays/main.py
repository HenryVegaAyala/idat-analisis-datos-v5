import matplotlib.pyplot as plt
from pydantic import color

mes = ["Enero", "Febrero", "Marzo", "Abril"]
luz = [40, 50, 45, 60]
agua = [25, 30, 31, 35]

plt.plot(mes, luz, label="servicios de Luz", marker="o", linewidth=3, color="blue")
plt.plot(mes, agua, label="servicios de agua", marker="s", linewidth=3, color="red")

plt.title("Gastos de la casa")
plt.xlabel("Mes")
plt.ylabel("Gastos S/.")

plt.grid(True, linestyle="--", color="k", linewidth=0.3)

for index, valor in enumerate(luz):
    plt.text(mes[index], valor + 1, str(valor), ha="center")

for index, valor in enumerate(agua):
    plt.text(mes[index], valor + 1, str(valor), ha="center")

# plt.show()
plt.savefig("Consolidado de gastos")