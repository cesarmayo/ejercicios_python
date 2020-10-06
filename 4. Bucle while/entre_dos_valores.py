"""
Escriba un programa que pida primero dos números enteros (mínimo y máximo) y que después pida números enteros situados entre ellos.
El programa terminará cuando se escriba un número que no esté comprendido entre los dos valores iniciales.
El programa termina escribiendo la cantidad de números escritos.
"""
print("=================")
print("ENTRE DOS VALORES")
print("=================")

contador = 0
valor_minimo = int(input("Escriba un numero: "))
valor_maximo = int(input(f"Escriba un numero mayor que {valor_minimo}: "))

while valor_maximo <= valor_minimo:
	valor_maximo = int(input(f"{valor_maximo} no es mayor que {valor_minimo}. Intentelo de nuevo: "))

numero = int(input(f"Escriba un numero entre {valor_minimo} y {valor_maximo}: "))

while (numero >= valor_minimo) and (numero <= valor_maximo):
	contador = contador + 1
	numero = int(input(f"escriba otro numero entre {valor_minimo} y {valor_maximo}: "))

if contador == 0:
	print(f"No ha escrito ningun numero entre {valor_minimo} y {valor_maximo}")
else:
	print(f"Se han escrito: {contador} numeros")

