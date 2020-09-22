# coding=utf-8
"""
Escriba un programa que pida una distancia en pies y que escriba esa distancia en centímetros.
Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.
"""
print("=================================")
print("CONVERTIDOR DE PIES A CENTIMETROS")
print("=================================")
dis = float(input("Ingrese la distancia es pies: "))

print(dis,"pies son",(dis*12)*2.54,"centimetros")