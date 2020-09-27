"""
Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba
que son iguales.
"""

print("=====================")
print("COMPARADOR DE NUMEROS")
print("=====================")

n1 = float(input("Ingrese un numero: "))
n2 = float(input("Ingrese otro numero: "))

if n1 > n2:
	print (f"Mayor: {n1}; Menor: {n2}")
elif n1 < n2:
	print (f"Mayor: {n2}; Menor: {n1}")
else:
	print("Los dos numeros son iguales")

