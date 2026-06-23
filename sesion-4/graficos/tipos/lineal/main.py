import matplotlib.pyplot as plt

semanas = [1, 2, 3, 4]
kilometros = [2, 5, 4, 8]

plt.plot(semanas, kilometros)
plt.title("Progreso de Juan")
plt.xlabel("semanas")
plt.ylabel("kilómetros recorridos")

plt.show()