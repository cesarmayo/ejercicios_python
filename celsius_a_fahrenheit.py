# coding=utf-8
"""
Escriba un programa que pida una temperatura en grados Celsius y que escriba esa temperatura en grados Fahrenheit.

Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32
"""
print("===================================")
print("CONVERTIDOR DE CELSIUS A FAHRENHEIT")
print("===================================")
cent = float(input("Ingrese temperatura (C°): "))

print(cent,"(C°) son",(1.8*cent)+32,"(F°)")
