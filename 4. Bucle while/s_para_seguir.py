"""
Escriba un programa que pida números pares mientras el usuario indique que quiere seguir introduciendo números.
Para indicar que quiere seguir escribiendo números, el usuario deberá contestar S o s a la pregunta.
"""
print("============")
print("CUENTA PARES")
print("============")
total = 0
npar = int(input("Escriba un numero par: "))
while npar%2 != 0:
	npar = int(input(f"{npar} no es un numero par. Intentelo de nuevo: "))
respuesta = input("¿Quiere escribir otro número par? (S/N): ")
total=1

while respuesta == 's' or respuesta =='S':
	npar = int(input("Escriba un numero par: "))
	while npar%2 != 0:
		npar = int(input(f"{npar} no es un numero par. Intentelo de nuevo: "))
	total = total + 1
	respuesta = input("¿Quiere escribir otro número par? (S/N): ")
print()
if total == 1:
	print(f"Ha escrito 1 numero par.")
else:
	print(f"Ha escrito {total} numeros pares.")
