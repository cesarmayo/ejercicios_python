"""
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y diga al final cuántos han sido pares y cuántos impares.
"""
print("===========================")
print("CONTADOR DE PARES E IMPARES")
print("===========================")

cont_pares = 0
cont_impares = 0

cant = int(input("Cuantos valores va a introducir: "))

if cant < 0:
	print("Imposible")
else:
	for i in range(1,cant+1):
		num = int(input("Escriba el valor: "))
		if num%2 == 0:
			cont_pares = cont_pares + 1
		else:
			cont_impares = cont_impares + 1

print(f"Ha escrito {cont_pares} pares y {cont_impares} impares")
print("Gracias por su colaboracion")