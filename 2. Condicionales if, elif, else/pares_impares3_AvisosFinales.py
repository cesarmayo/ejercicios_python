"""
Escriba un programa que pida primero un número par y a continuación un numero impar (positivos o negativos). 
En caso de que uno o los dos valores no sean correctos, se mostrarán uno o dos avisos.
"""

print("===========")
print("PAR E IMPAR")
print("===========")

par = int(input("Escriba un numero par: "))
impar = int(input("Escriba un numero impar: "))
mensaje_error = False

if par%2 == 1:
	print("No ha escrito un numero par")
	mensaje_error = True

if impar%2 == 0:
	print("No ha escrito un numero impar")
	mensaje_error = True

if mensaje_error:
	print("Ejecute de nuevo el programa para volver a intentarlo.")
else:
	print("Gracias por su colaboracion.")


