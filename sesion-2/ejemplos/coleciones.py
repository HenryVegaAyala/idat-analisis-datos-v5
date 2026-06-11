# 1. Crear una lista de productos: Ejemplo de lista de cadenas o strings
vitrina = ["Pan", "Alfajor", "Aceite", "Mantequilla"]

# 2. Ejemplo de lista de números enteros o int
ventas_hora = [10, 20, 15, 30]

# 3. Ejemplo de lista de valores mixtos
valores_mixtos = [10, 20.25, "Hola", 'Mundo', True, False]

# 4. Acceder a un elemento de una lista basado en índice
primer_producto = vitrina[0]
print(f"Primer producto: {primer_producto}")

# 5. Acceder al último elemento de una lista
ultimo_producto = vitrina[-1]
print(f"Ultimo producto: {ultimo_producto}")

# 6. Agregar un nuevo producto a la lista
vitrina.append("Donut")
print(f"Lista de productos agregados: {vitrina}")

# 7. Cambiar o actualizar un producto de la lista
vitrina[2] = "Aceite de oliva"
print(f"Lista de productos actualizada: {vitrina}")

# 8. Eliminar un producto de la lista
vitrina.remove("Pan")
print(f"Lista de productos eliminados: {vitrina}")

# 9. Eliminar un producto basado en el índice de una lista
del vitrina[0]
print(f"Lista de productos eliminados: {vitrina}")

# 10. Contar elementos que existe en una lista
total_productos = len(vitrina)
print(f"Total de productos en la vitrina: {total_productos}")