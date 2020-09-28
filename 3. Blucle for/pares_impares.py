print("======================================")
print("| DETECTOR DE NUMERO PARES O IMPARES |")
print("======================================")

n1 = int(input("Escriba un numero entero: "))
n2 = int(input(f"Escriba un numero entero mayor o igual que {n1}: "))

if n1 > n2:
	print(f"Le he pedido un numero mayor que {n1}")
else:
	for i in range(n1,n2+1):
		if (i%2==0):
			print(f"El numero {i} es par")
		else:
			print(f"El numero {i} es impar")


