class Analista:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo_inicial(self):
        return f"{self.nombre} te da la bienvenida a la clase de Python"

analista_1 = Analista("Jorge", "Chavez")
print(analista_1.saludo_inicial())