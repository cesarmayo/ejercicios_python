"""
Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si
la división es exacta o no. Debe tomar en cuenta que no se puede dividir por cero.
"""
print("==================")
print("DIVISOR DE NUMEROS")
print("==================")

dividendo = int(input("Escriba el dividiendo: "))
divisor = int(input("Escriba el divisor: "))

if divisor == 0:
	print("No se puede dividir por cero!")
elif dividendo % divisor == 0:
	print(f"la vivision es exacta. cociente {dividendo // divisor}")
else:
	print(f"La división no es exacta. Cociente: {dividendo // divisor} "f"Resto: {dividendo % divisor}")


