"""
Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
"""
print("==================")
print("COMPARADOR DE AÑOS")
print("==================")
nmayor = 0


n1 = int(input("Escriba un numero: "))
n2 = int(input("Escriba otro numero: "))


if n1 > n2:
	nmayor = n1
	nmenor = n2
else:
	nmayor = n2
	nmenor = n1

if nmayor%nmenor == 0:
	print(f"{nmayor} es multiplo de {nmenor}")
else:
	print(f"{nmayor} no es multiplo de {nmenor}")