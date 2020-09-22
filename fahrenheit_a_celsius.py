# coding=utf-8
"""
Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa temperatura en grados Celsius
Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: C = (F - 32) / 1,8
"""
print("===================================")
print("CONVERTIDOR DE FAHRENHEIT A CELSIUS")
print("===================================")
fahr = float(input("Ingrese termperatura (F°): "))
print(fahr,"(F°) son",(fahr-32) / 1.8,"(C°)")