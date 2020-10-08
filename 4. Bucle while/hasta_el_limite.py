"""
Escriba un programa que pida un valor límite positivo y a continuación pida números hasta que la suma de los números
introducidos supere el límite inicial.
"""

print("==============")
print("HASTA EL LIMTE")
print("==============")
total = 0
limite = float(input("Escriba el valor limite: "))


while limite < 0:
	limite = float(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))

print()

while total < limite:
	numero = float(input("Escriba un numero: "))
	total = total + numero

print()

print(f"Ha superado el limite. la suma de numeros introducidos es: {total}")