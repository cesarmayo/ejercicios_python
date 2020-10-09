"""
Escriba un programa que pida primero dos números enteros (mínimo y máximo) y que después pida números enteros situados entre ellos.
El programa terminará cuando se escriba un número que no esté comprendido entre los dos valores iniciales.
El programa termina escribiendo la cantidad de números escritos.
"""
print("=================")
print("ENTRE DOS VALORES")
print("=================")

total=0
minimo = int(input("Escriba un numero: "))
maximo = int(input(f"Escriba otro numero mayor que {minimo}: "))

while maximo <= minimo:
	maximo = int(input(f"{maximo} no es mayor que {minimo}. Intentelo de nuevo: "))

numero = int(input(f"Escriba un numero entre {minimo} y {maximo}: "))

while (numero > minimo) and (numero < maximo):
	total = total + 1
	numero = int(input(f"Escriba otro numero entre {minimo} y {maximo}: "))

print()

if total <= 0:
	print(f"Usted no ha escrito ningun numero entre {minimo} y {maximo}")
elif total == 1:
	print(f"Usted ha escrito {total} numero entre {minimo} y {maximo}")
else:
	print(f"Usted ha escrito {total} numeros entre {minimo} y {maximo}")
