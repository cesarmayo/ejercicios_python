"""
Crear un programa que permita al usuario ingresar titulos de libros por teclado,finalizando el ingreso al
leerse el string "*" (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga solo
la barra ("/") se considera que termina la linea.
Por cada linea informar cuanto digitos numericos (del 0 al 9) aparecieron en total (en todos los titulos
de libros que componen esa linea).
Finalmente informar cuantas lineas completas se ingresaron

ejemplo:

Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
libro:/
Linea completa. Aparecen 2 digitos numericos

Libro: 20000 leguas de viaje submarino
libro: El senor de los anillos
libro:/
Linea completa. Aparecen 5 digitos numericos

Libro: 20 anos despues
libro:*
Fin. Se leyeron 2 lineas completas

"""

digitos_en_la_linea = 0
cant_lineas = 0

titulo = input("libro: ")
while titulo != "*":
	if titulo == "/":
		cant_lineas+=1
		print(f"Linea completa. Aparecen {digitos_en_la_linea} digitos")
		digitos_en_la_linea=0
	else:
		for caracter in titulo:
			if caracter in "0123456789":
				digitos_en_la_linea += 1
	titulo = input("libro: ")
print (f"Fin. Se leyeron {cant_lineas} lineas" )