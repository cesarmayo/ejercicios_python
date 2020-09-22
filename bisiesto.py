# coding=utf-8
"""
Programa que permite saber si un ano es bisiesto
"""

print("****AÑO BISIESTO****")

anno = int(input("Ingrese año: "))
if anno%4 !=0:
	print("No es un año bisiesto")
elif anno%100 != 0 or anno%400 ==0:
	print("Si es una año bisiesto")
else:
	print("No es un año bisiesto")
