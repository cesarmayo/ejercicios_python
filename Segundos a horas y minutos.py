"""
Escriba un programa que pida una cantidade de segundos y escriba cuantas
hora, minutos y segundos son
"""
print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")
seg = int(input("Escriba una cantidad en segundos: "))
horas = seg//3600
temp = seg%3600
minutos = temp//60
segundos = temp%60
print(seg,"segundos son",horas,"horas,",minutos,"minutos y", segundos, "segundos")

