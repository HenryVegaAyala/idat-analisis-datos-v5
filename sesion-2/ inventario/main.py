class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock = self.stock + (cantidad)
        print(f"El stock actual del {self.nombre} fue actualizado: {self.stock}")


p1 = Producto("Laptops", 1500, 10)
p1.actualizar_stock(5) # Agrege 5 laptops al stock
p1.actualizar_stock(-3) # Vendí 3 laptops, por lo tanto resto
