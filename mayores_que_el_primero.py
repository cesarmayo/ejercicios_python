"""
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y
muestre un mensaje cada vez que un número no sea mayor que el primero.
"""
print("======================")
print("MAYORES QUE EL PRIMERO")
print("======================")
cant = int(input("Cuanto numeros se van a introducir: "))
num = int(input("Escriba un numero: "))

for j in range(2,cant+1):
	nums = int(input(f"Escriba un numero mas gande que {num}: "))
	if num > nums:
		print (f"No es mas gande que {num}")