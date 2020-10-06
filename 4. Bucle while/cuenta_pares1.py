"""
Escriba un programa que pida números pares mientras el usuario indique que quiere seguir introduciendo números.
Para indicar que quiere seguir escribiendo números, el usuario deberá contestar S o s a la pregunta.
"""

print("============")
print("CUENTA PARES")
print("============")
npar = int(input("Escriba un numero par: "))
while npar%2 != 0:
	npar = int(input(f"{npar} no es un numero par. Intentelo de nuevo: "))
contador = 1
respuesta =input("¿Quiere escribir otro número par? (S/N): ")



while respuesta == 's' or respuesta == 'S':
	npar = int(input("Escriba un numero par: "))
	while npar%2 != 0:
		npar = int(input(f"{npar} no es un numero par. Intentelo de nuevo: "))
	contador = contador + 1
	respuesta =input("¿Quiere escribir otro número par? (S/N): ")

print()
if contador == 1:
	print("Ha escrito un 1 par")
else:
	print(f"Ha escrito {contador} numeros pares.")

