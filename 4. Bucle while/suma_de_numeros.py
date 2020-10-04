"""
Escriba un programa que permita totalizar la cantidad de numeros enteros positivos
ingresados hasta que el usuario escriba el numero cero.
"""

print("=========================")
print("SUMA DE NUMEROS POSITIVOS")
print("=========================")

total = 0
numero = int(input("Escriba un numero, (0 para terminar): "))
while numero != 0:
	total+= numero #total = total + numero
	numero = int(input("Escriba un numero, (0 para terminar): "))
print(f"Total: {total}")
