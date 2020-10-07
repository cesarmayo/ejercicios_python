"""
Escriba un programa que pida números enteros mientras sean cada vez más grandes.
"""
print("====================")
print("CADA VEZ MAS GRANDES")
print("====================")

n1 = int(input("Escriba un numero: "))
n2 = int(input(f"Escriba un numero mayor que {n1}: "))

while n2 > n1:
	n1 = n2
	n2 = int(input(f"Escriba un numero mayor que {n1}: "))

print()
print(f"{n2} no es mayor que {n1}")

	


