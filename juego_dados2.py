# coding=utf-8
"""
Escriba un programa que simule un juego en el que dos jugadores (Carmen y David) tiran dos dados. El que saque mayor puntuación
total, gana. Si la puntuación total coincide, gana quien haya sacado el dado con el valor más alto. Si el valor más alto también
coincide, empatan.
"""
import random

input("Es el turno de Carmen. Presione enter.")
tiro_carmen_dado1 =(random.randint(1, 6))
tiro_carmen_dado2 =(random.randint(1, 6))
total_carmen = tiro_carmen_dado1 + tiro_carmen_dado2

input("Es el turno de David. Presione enter.")
tiro_david_dado1 =(random.randint(1, 6))
tiro_david_dado2 =(random.randint(1, 6))
total_david = tiro_david_dado1 + tiro_david_dado2


print("Carmen ha sacado un",tiro_carmen_dado1,"y un",tiro_carmen_dado2)
print("David ha sacado un",tiro_david_dado1,"y un",tiro_david_dado2)

if total_carmen == total_david:
	print("Han empatado")
elif total_carmen > total_david:
	print("Ha ganado Carmen!")
else:
	print("Ha ganado David!")