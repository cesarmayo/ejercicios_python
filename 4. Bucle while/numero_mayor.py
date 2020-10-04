"""
Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo
número mientras no sea mayor que el primero. El programa terminará escribiendo los dos números.
"""
print("============")
print("NUMERO MAYOR")
print("============")

print()

primero = int(input("Ingrese un numero: "))
segundo = int(input("Ingrese un numero: "))

while primero >= segundo:
	segundo = int(input(f"{primero} no es mayor que {segundo}. Inténtelo de nuevo: "))

print()

print(f"Los numeros que ha escrito son {primero} y {segundo}")

print()

