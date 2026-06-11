
class Analista:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo_inicial(self):
        resultad =  f"{self.nombre} {self.apellido} te da la bienvenida"
        print(resultad)

    def despedida(self):
        resultad = f"Adios {self.nombre} {self.apellido}, hasta luego"
        print(resultad)