"""
Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
Mejore el programa anterior haciendo que el programa avise cuando se escriben valores negativos o nulos.
"""
print("=======================")
print("COMPARADOR DE MULTIPLOS")
print("=======================")
 
nmayor = 0
nmenor = 0


n1 = int(input("Escriba un numero: "))
n2 = int(input("Escriba otro numero: "))

if n1<0 or n2<0:
	print("Lo siento. Este programa no admite valores negativos")
elif n1==0 or n2 == 0:
	print("Este programa no admite valores nulos")
elif n1 > n2 and n1%n2==0:
	print(f"{n1} es multiplo de {n2}")
elif n1 > n2 and n1%n2!=0:
	print(f"{n1} no es multiplo de {n2}")
elif n2 > n1 and n2%n1==0:
	print(f"{n2} es multiplo de {n1}")
elif n2 > n1 and n2%n1!=0:
	print(f"{n2} no es multiplo de {n1}")






	