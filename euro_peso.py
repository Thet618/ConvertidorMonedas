
euros = float(input("Ingresa la cantidad en euros: "))
tipo_cambio = float(input("Ingresa el tipo de cambio (pesos por euro): "))

# Conversión
pesos = euros * tipo_cambio

# Mostrar resultado
print(f"{euros} euros equivalen a {pesos} pesos")
