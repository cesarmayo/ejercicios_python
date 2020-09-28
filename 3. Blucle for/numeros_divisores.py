"""
Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
"""
print("=====================")
print("| NUMEROS DIVISORES |")
print("=====================")

n1 = int(input("Ingrese un numero mayo a cero: "))
if n1<=0:
	print("El numero que ingreso es menor que el cero.")
else:
	print(f"Los divisores de {n1} son:", end="")
	for i in range(1,n1):
		if (n1%i == 0):
			print(i, end=", ")