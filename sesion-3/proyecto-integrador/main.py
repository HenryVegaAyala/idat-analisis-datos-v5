import numpy as np


class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self):
        notas = np.array(self.notas)
        promedio = np.mean(notas)

        if promedio > 10:
            print(f"El alumno {self.nombre} tiene un promedio de {promedio:.1f}, aprobó")
        else:
            print(f"El alumno {self.nombre} tiene un promedio de {promedio:.1f}, desaprobó")


# Ejemplo de uso
estudiante = Estudiante("Pepito", [10, 12, 9, 15])
estudiante.calcular_promedio()
