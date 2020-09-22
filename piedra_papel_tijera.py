# coding=utf-8
"""
Escriba un programa que simule el juego Piedra, papel, tijera para dos jugadores (Inés y Juan).

Las reglas del juego son las siguientes:

Simultáneamente, los dos jugadores muestran una mano en tres posibles posiciones:
Piedra: se muestra el puño cerrado.
Papel: se muestra la palma de la mano.
Tijera: se muestra la palma de la mano con los dedos separados en dos grupos.
El jugador que ha sacado Piedra gana al jugador que ha sacado Tijera.
El jugador que ha sacado Tijera gana al jugador que ha sacado Papel.
El jugador que ha sacado Papel gana al jugador que ha sacado Piedra.
Noticia relacionada: Robot que gana siempre a este juego (septiembre de 2015).
Resuelva este ejercicio utilizando la función random.randrange(), de manera que el valor 1 corresponda a Piedra, el valor 2 corresponda
a papel y el valor 3 corresponda a Tijera.
"""
import random

print("***JUEGO DE PIEDRA, PAPEL Y TIJERA***")
print(input("Es el turno de Ines. Presione enter para continuar."))
opcion_ines = random.randrange(1,4)
opcion_juan = random.randrange(1,4)

if opcion_ines == 1:
	opcion_ines = "piedra"
elif opcion_ines == 2:
	opcion_ines = "papel"
elif opcion_ines == 3:
	opcion_ines = "tijera"

if opcion_juan == 1:
	opcion_juan = "piedra"
elif opcion_juan == 2:
	opcion_juan = "papel"
elif opcion_juan == 3:
	opcion_juan = "tijera"

print("Ines saca la opcion:",opcion_ines)
print("Juan saca la opcion:",opcion_juan)


if opcion_ines == opcion_juan:
	print("Empate..!")
#El jugador que ha sacado Piedra gana al jugador que ha sacado Tijera.
elif opcion_ines == "piedra" and opcion_juan == "tijera":
	print("Ha ganado Ines..!")
#El jugador que ha sacado Tijera gana al jugador que ha sacado Papel.
elif opcion_ines == "tijera" and opcion_juan == "papel":
	print("Ha ganado Ines..!")
#El jugador que ha sacado Papel gana al jugador que ha sacado Piedra.
elif opcion_ines == "papel" and opcion_juan == "piedra":
	print("Ha ganado Ines..!")
else:
	print("Ha ganado Juan")



