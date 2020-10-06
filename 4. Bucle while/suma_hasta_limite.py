"""
Escriba un programa que pida un valor límite positivo y a continuación pida números hasta que la suma de los números
introducidos supere el límite inicial.
"""

print("===============")
print("HASTA EL LIMITE")
print("===============")

suma = 0

valor_limite = float(input("Ingrese el valor limite: "))
while valor_limite <= 0:
	valor_limite = float(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))

while valor_limite > suma:
	print()
	numero = float(input("Ingrese numero: "))
	suma = suma + numero


print()
print(f"Ha superado el límite. La suma de los números introducidos es: {suma}")
