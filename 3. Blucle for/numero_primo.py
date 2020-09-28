numero = int(input("Ingrese un numero mayor que uno: "))
contador = 0
for i in range(1,numero+1):
	if numero%i == 0:
		contador = contador + 1
if contador <= 2:
	print(f"{numero} es primo")
else:
	print(f"{numero} no es primo")
