"""
Escriba un programa que pida números enteros mientras sean cada vez más grandes.
"""

primero = int(input("Escriba un numero: "))
segundo =int(input(f"Escriba un número mayor que {primero}: "))
while primero <= segundo:
	primero = segundo
	segundo =int(input(f"Escriba un número mayor que {segundo}: "))
print(f"{segundo} no es mayor que {primero}")
	


