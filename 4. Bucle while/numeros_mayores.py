"""
Escriba un programa que pida números decimales mientras el usuario escriba número mayores
que el primero.
"""

print("===============")
print("NUMEROS MAYORES")
print("===============")

n1 = float(input("Escriba un numero: "))
n2 = float(input(f"Escriba un numero mayor que {n1}: "))

while n2 > n1:
	n2 = float(input(f"Escriba un numero mayor que {n1}: "))

print()

print(f"{n2} no es mayor que {n1}.")
	
	