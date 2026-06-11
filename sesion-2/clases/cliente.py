class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def comprar(self, nombre_producto, monto_producto):
        if self.saldo >= monto_producto:
            self.saldo -= monto_producto  ## --> self.saldo = self.saldo - monto_producto
            print(f"{nombre_producto} comprado por {self.nombre}. Saldo restante: {self.saldo}")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para comprar {nombre_producto}. Saldo actual: {self.saldo}")

# Ejemplo de uso
cliente_1 = Cliente("Juan", 500)
cliente_1.comprar("Laptop", 200)
cliente_1.comprar("Mouse", 100)
cliente_1.comprar("Celular", 250)
cliente_1.comprar("Teclado", 100)
