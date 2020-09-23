# coding=utf-8
"""
Escriba un programa que simule un juego en el que dos jugadores (Gloria y Héctor) sacan tres cartas al azar del 1 al 10.
Gana el jugador que obtenga la mayor puntuación total, siempre que no se pase de quince, en cuyo caso el jugador pierde.
"""
import random

print("==============")
print("JUEGO DE DADOS")
print("==============")

total_gloria = 0
total_hector = 0
raw_input("Turno de Gloria. Presione Enter para continuar...")
raw_input("Turno de Hector. Presione Enter para continuar...")


for x in range (3):
	tiro_gloria_dado =(random.randint(1, 6))
	print(x+1,")Tiro de Gloria:",tiro_gloria_dado)
	total_gloria = total_gloria + tiro_gloria_dado
print("Total:",total_gloria)

for x in range (3):
	tiro_hector_dado =(random.randint(1, 6))
	print(x+1,")Tiro de Hector:",tiro_hector_dado)
	total_hector = total_hector + tiro_hector_dado
print("Total:",total_hector)

if total_gloria == total_hector:
	print("Han empatado")
else:
	if total_gloria > 15:
		print("Gana Hector!")
	elif total_hector >15:
		print("Gana Gloria")
	elif total_gloria > total_hector and total_gloria <=15 :
		print("Gana Gloria..!")
	elif total_hector > total_gloria and total_hector <=15 :
		print("Gana Hector..!")

