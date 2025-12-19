tipo_cambio = 17.00  # 17 mxn = 1 usd (ejemplo)

pesos = float(input("Ingresa la cantidad en pesos mexicanos: "))
dolares = pesos * tipo_cambio


print(f"${dolares} USD equivalen a ${pesos:.2f} $pesos MX")