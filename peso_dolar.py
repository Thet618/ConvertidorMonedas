tipo_cambio = 17.00  # 1 USD = 17 MXN (ejemplo)

pesos = float(input("Ingresa la cantidad en pesos mexicanos: "))
dolares = pesos / tipo_cambio


print(f"${pesos} MXN equivalen a ${dolares:.2f} USD")
