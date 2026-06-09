# if: "Si pasa esto..."
# elif: "si no pasó lo anterior, prueba esto..."
# else: "Si nada cumple"

# If else
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# If elif else
nota = 15
if nota >= 18: # Primera condicional
    print("Excelente")
elif nota >= 13: # Segunda condicional
    print("Aprobado")
else:
    print("Desaprobado") # Caso final si ninguna cumple
