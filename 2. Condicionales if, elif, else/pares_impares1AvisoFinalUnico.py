"""
Escriba un programa que pida primero un número par y luego un número impar (positivos o negativos). En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.
"""
print("===========")
print("PAR E IMPAR")
print("===========")

par = int(input("Escriba un numero par: "))
impar = int(input("Escriba un numero impar: "))

if (par%2 == 0) and (impar%2 == 1):
	print("¡Gracias por su colaboracion!")
else: 
	print("Uno o mas de los valores que ha escrito no son correctos. Ejecute de nuevo el programa para volver a interntarlo.")



