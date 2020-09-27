"""
Escriba un programa que pida primero un número par (positivo o negativo) y si el valor no es correcto, muestre un aviso. 
Si el valor es correcto, pedirá un número impar (positivo o negativo) y si el valor no es correcto, mostrará un aviso.
"""
print("===========")
print("PAR E IMPAR")
print("===========")

par = int(input("Escriba un numero par: "))
impar = int(input("Escriba un numero impar:"))

if par%2 != 0:
	print("No ha escrito un numero par.")
	print("Ejecute de nuevo el programa para volver a intentarlo.")
elif impar%2 != 1:
	print("No ha escrito un numero impar.")
	print("Ejecute de nuevo el programa para volver a intentarlo.")
else:
	print("¡Gracias por su colaboración!")
