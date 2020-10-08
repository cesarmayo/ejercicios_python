"""
Escriba un programa que pida la cantidad de números positivos que se tienen que escribir y
a continuación pida números hasta que se haya escrito la cantidad de números positivos indicada.
"""
print("=================")
print("NUMEROS POSITIVOS")
print("=================")



objetivo = int(input("Ingrese la cantidad de numeros positivos a escribir: "))

while objetivo <=0:
	objetivo = int(input("La cantidad debe ser mayor que 0. Inténtelo de nuevo: "))

numero = int(input("Escriba un numero: "))
total = 1

if numero > 0:
    cantidad = 1
else:
    cantidad = 0

while cantidad < objetivo:
    numero = int(input("Escriba otro número: "))
    if numero > 0:
        cantidad += 1
    total += 1

print()
if total == 1:
    print("Ha escrito 1 número positivo.")
elif objetivo == 1:
    print(f"Ha escrito {total} números, {objetivo} de ellos positivo.")
else:
    print(f"Ha escrito {total} números, {objetivo} de ellos positivos.")

	