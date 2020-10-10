"""
Crea un programa que solicite el ingreso de numeros enteros positivos, hasta que el usuario ingrese el 0.
Por cada numero, informar cuantos digitos pares y cuantos impares tiene. Al finalizar, informar la cantidad
de digitos pares y de digitos impares leidos en total
"""

par = 0
impar = 0

numero = int(input("Ingrese un numero entero positivo: "))

while numero > 0:
	numero = int(input("Ingrese otro numero entero positivo: "))
	if numero%2 == 0:
		par = par + 1
	else:
		impar = impar + 1

print("Cantidad de numeros pares: ",par)
print("Cantidad de numeros impares: ",impar)



