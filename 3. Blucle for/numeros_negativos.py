"""
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba
cuántos negativos ha introducido.
"""
print("=================")
print("NUMEROS NEGATIVOS")
print("=================")

contador=0

num  = int(input("Cuantos valores va a introducir?: "))

for i in range(1,num+1):
	nums = int(input(f"Escriba el numero {i}: "))
	if nums < 0:
		contador = contador + 1

if num > 0:
	if contador == 1:
		print(f"Ha escrito {contador} numero negativo")
	else:
		print(f"Ha escrito {contador} numeros negativos")
else:
	print("No ha escrito ningun numero negativo")





