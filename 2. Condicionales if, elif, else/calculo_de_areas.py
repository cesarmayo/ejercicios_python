"""
Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que
pedir entonces la base y la altura y escribir el área. 
Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir
entonces el radio y escribir el área.

Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo
es Pi (aproximadamente 3,141592) por el radio al cuadrado.
"""
print("================")
print("CALCULO DE AREAS")
print("================")

print("Elija la fugura geometrica:")
print("a) Triangulo")
print("b) Circulo")
fig = input("¿Qué figura quiere calcular (Escriba a) o b)?: ")
fig = fig.lower()




if fig == "a":
	base = float(input("Ingrese la base del triangulo: "))
	altura = float(input("Ingrese la altura del triangulo: "))
	area_triangulo=(base*altura)/2
	print (f"Un triangulo de base {base} y altura {altura} tiene un area de: {area_triangulo}")

elif fig  == "b":
	radio = float(input("Ingrese el radio del circulo: "))
	area_circulo = (3.141592*(radio**2))
	print(f"Un circulo de radio {radio} tiene un area de: {area_circulo}")
else:
	print("Opcion invalida")
