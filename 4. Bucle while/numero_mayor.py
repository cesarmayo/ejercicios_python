"""
Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo
número mientras no sea mayor que el primero. El programa terminará escribiendo los dos números.
"""
print("============")
print("NUMERO MAYOR")
print("============")

print()

n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero entero: "))

while n2 <= n1:
	n2 = int(input(f"*{n1} no es mayor que {n2}. Ingrese otro numero: "))

print()

print(f"Los numero que ha escrito son {n1} y {n2}")
