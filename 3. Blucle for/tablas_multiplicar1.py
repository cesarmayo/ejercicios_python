import random
"""
Escriba un programa que genere una multiplicación de dos números del 2 al 10 al azar,
pregunte por el resultado y diga si se ha dado la respuesta correcta. El programa 
debe pedir primero al usuario cuántas multiplicaciones se van a plantear.

Amplíe el programa haciendo que lleve la cuenta de las respuestas correctas e incorrectas
e indique la nota correspondiente. Si la nota es igual o mayor que 9, el programa felicitará
al usuario por el resultado.
"""
r_correcta = 0
r_incorrecta = 0

preguntas = int(input("Número de preguntas: "))
if preguntas <=0:
	print("El número de preguntas debe ser al menos 1.")
else:
	for i in range(preguntas):
		n1 = random.randint(2, 10)
		n2 = random.randint(2, 10)
		respuesta = int(input(f"¿Cuánto es {n1} x {n2}?: "))
		resultado = n1 * n2
		if respuesta == resultado:
			print("Respuesta correcta..!")
			r_correcta = r_correcta + 1
		else:
			print("Respuesta incorrecta..!")
			r_incorrecta = r_incorrecta + 1

	print(f"Ha contestado correctamente {r_correcta} pregunta.")
	nota = (r_correcta * 10)/preguntas
	if nota > 9:
		print(f"Le corresponde una nota de {nota}")
		print("Felicitaciones por el resultado..!")
	else:
		print(f"Le corresponde una nota de {nota}")