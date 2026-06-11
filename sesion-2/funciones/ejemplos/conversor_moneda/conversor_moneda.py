def convertir_a_soles(dolares, tipo_de_cambio = 3.5):
    conversion_soles = dolares * tipo_de_cambio
    return conversion_soles

# Caso 1 - Dólares y tipo de cambio por defecto
resultado = convertir_a_soles(100)
print(f"Resultado: {resultado}")

# Caso 2 - Dólares y nuevo tipo de cambio
resultado = convertir_a_soles(100, 3.6)
print(f"Resultado: {resultado}")