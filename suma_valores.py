"""
Escriba un programa que pregunte cuantos números se van a introducir, pida esos
números (que puedan ser decimales) y calcule su suma.
"""
print("===============")
print("SUMA DE VALORES")
print("===============")
acumulador = 0
numval =  int(input("Cuantos valores va a introducir: "))
if (numval < 0): 
	print("Imposible realizar operacion")
else:
	for i in range(1,numval+1):
		num = float(input(f"Escriba el numero ({i}): "))
		acumulador = acumulador + num
	print("La suma de los numeros que ha escrito es: ",acumulador) 