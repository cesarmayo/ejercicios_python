"""
Escriba un programa que pida un número entero mayor que cero y calcule su factorial.
"""


print("======================")
print("FACTORIAL DE UN NUMERO")
print("======================")

factorial = 1

numero = int(input("Ingrese un numero: "))

if numero<0:
	print("Imposible")
else: 
	for i in range (1,numero+1):
		factorial = (factorial * i)
	print(f"El factorial de {numero} es: {factorial}")