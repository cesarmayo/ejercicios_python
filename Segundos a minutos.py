# coding=utf-8
"""
Escriba un programa que pida una cantidad de segundos y escriba cuantos
minutos y segundos son.
"""
print("---------------------------------")
print("CONVERTIDOR DE SEGUNDOS A MINUTOS")
print("---------------------------------")
seg = int(input("Escriba una cantidad de segundos: "))
print(seg,"segundos son", (seg//60), "minutos y", (seg%60), "segundos") 
