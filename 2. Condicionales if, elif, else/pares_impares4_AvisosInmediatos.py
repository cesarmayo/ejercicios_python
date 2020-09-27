"""
Escriba un programa que pida primero un número par y a continuación un numero impar (positivos o negativos). 
En cada petición, si el valor no es correcto se mostrará un aviso.
"""
print("===========")
print("PAR E IMPAR")
print("===========")

mensaje_error = False
par = int(input("Escriba un numero par: "))
impar = int(input("Escriba un numero impar: "))

if par%2 != 0:
	print("No ha escrito un numero par!")
	mensaje_error = True

if impar%2 != 1:
	print("No ha escrito un numero impar!")
	mensaje_error = True

if mensaje_error:
	print("Ejecute de nuevo el programa para volver a intentarlo!")
else:
	print("Gracias por su colaboracion")