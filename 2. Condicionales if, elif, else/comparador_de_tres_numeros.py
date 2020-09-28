"""
Escriba un programa que pida tres números y que escriba si son los tres iguales, 
si hay dos iguales o si son los tres distintos.
"""

print("==========================")
print("COMPARADOR DE TRES NUMEROS")
print("==========================")

n1 = int(input("Escriba un numero: "))
n2 = int(input("Escriba otro numero: "))
n3 = int(input("Escriba otro numero mas: "))

if n1 == n2 and n1 == n3:
	print("Hay tres numeros iguales: ")
elif n1 == n2 or n1==n3 or n2==n3:
	print ("Hay dos numeros iguales: ")
else:
	print("Los tres numeros que ha escrito son distintos")
