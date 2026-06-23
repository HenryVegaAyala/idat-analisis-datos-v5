import matplotlib.pyplot as plt

horas = [1, 2, 3, 4]
cantidad = [10, 20, 25, 30]

plt.plot(horas, cantidad)
plt.title("Ventas de café")
plt.xlabel("Horas del día")
plt.ylabel("Cantidad de café vendido")

plt.show()
