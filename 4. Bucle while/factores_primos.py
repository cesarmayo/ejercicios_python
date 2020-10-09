"""
Escriba un programa que calcule la descomposición en factores primos de un número.
"""
print("==============================================")
print("DESCOMPISICION DE UN NUMERO EN FACTORES PRIMOS")
print("==============================================")

numero = int(input("Ingrese un numero mayor que cero: "))

while numero <= 0:
	numero = int(input("El numero que ingreso no es mayor que cero. Intentelo de nuevo: "))

for i in range(2,numero+1):
	while numero%i == 0:
		numero = numero // i
		print(f"{i}", end="")

