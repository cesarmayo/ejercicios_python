"""
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y escriba el mayor,
el menor y la media aritmética. Se recuerda que la media aritmética de un conjunto de valores es la suma de
esos valores dividida por la cantidad de valores.
"""

print("================================")
print("MAYOR - MENOR - MEDIA ARITMETICA")
print("================================")

cant = int(input("Ingrese la cantida de numeros a introducir: "))
if cant <=0:
	print("Imposible..!")
else:
	numero = float(input("Ingrese el numero 1: "))
	nmayor = numero
	nmenor = numero
	suma = numero
	for i in range(2, cant+1):
		numero = float(input(f"Ingrese el numero {i}: "))
		suma = suma + numero
		if numero < nmenor:
			nmenor = numero
		if numero > nmayor:
			nmayor = numero
	print(f"El numero menor es: {nmenor}")
	print(f"El numero mayor es: {nmayor}")
	print(f"La media aritrmetica es:{suma/cant}")
