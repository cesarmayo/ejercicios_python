# coding=utf-8
"""
Escriba un programa que simule un juego en el que dos jugadores (Álvaro y Bárbara) tiran un dado. El que saque el valor más alto,
gana. Si la puntuación coincide, empatan.
"""
import random
print("==============")
print("JUEGO DE DADOS")
print("==============")
input("Turno de Alvaro. presione enter..!")
tiro_alvaro =(random.randint(1, 6))
print("Alvaro ha sacado el numero: ",tiro_alvaro)
tiro_barbara =(random.randint(1, 6))
print("Barbara ha sacado el numero: ",tiro_barbara)

if tiro_alvaro != tiro_barbara:
	if tiro_alvaro > tiro_barbara:
		print("Alvaro es el ganador..!")
	else:
		print("Barbara es la ganadora..!")
else:
	print("Hubo un empate..!")
