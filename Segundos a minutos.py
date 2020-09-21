"""
Escriba un programa que pida una cantidad de segundos y escriba cuantos
minutos y segundos son.
"""
print("CONVERTIDOR DE SEGUNDOS A MINUTOS")
seg = int(input("Escriba una cantidad de segundos: "))
print(seg,"segundos son", (seg//60), "minutos y", (seg%60), "segundos") 
