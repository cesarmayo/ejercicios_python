"""
Escriba un programa que pida números mientras no se escriba un número negativo. El programa terminará escribiendo
la suma de los números introducidos.
"""
total=0


numero = int(input("Escriba un numero: "))
while numero > 0:
	total = total + numero
	numero = int(input("Escriba un numero: "))
	

print("La suma de los numeros es positivos es: ", total)