"""
Crea un programa que solicite el ingreso de numeros enteros positivos, hasta que el usuario ingrese el 0.
Por cada numero, informar cuantos digitos pares y cuantos impares tiene. Al finalizar, informar la cantidad
de digitos pares y de digitos impares leidos en total
"""

total_pares = 0
total_impares = 0

numero = int(input("Ingrese un numero entero positivo: "))

while numero != 0:
	pares = 0
	impares = 0
	while numero != 0:
		ultimo_digito = numero%10
		if ultimo_digito%2 == 0:
			pares=+1
		else:
			impares+=1
		numero = numero // 10

	print(f"El numero ingresado tiene {pares} digitos pares y {impares} digitos impares")
	numero = int(input("Ingrese un numero entero positivo: "))




