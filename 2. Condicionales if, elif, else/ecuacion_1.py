"""
Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0)
y escriba la solución. Se recuerda que una ecuación de primer grado puede no tener solución,
tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula
de las soluciones es x = -b / a.
"""
x=0
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))


if a == 0:
	print("La ecuación no tiene solucion")
elif b == 0 and a == 0:
	print("Todos los numeros son solucion")
else:
	x=(-b)/a
	print(f"La ecuacion tiene una solucion: {x}")
