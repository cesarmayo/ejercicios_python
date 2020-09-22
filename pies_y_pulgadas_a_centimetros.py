# coding=utf-8
"""
Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en centímetros.

Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.
"""
print("============================================")
print("CONVERTIDOR DE PIES Y PULGADAS A CENTÍMETROS")
print("============================================")
pi = float(input("Ingrese distancia en pies: "))
pulg = float(input("Ingrese distancia en pulgadas: "))

pies_cm = (pi*12)*2.54
pulgadas_cm = (pulg*2.54)
totalcm = pulgadas_cm + pies_cm

print(pi,"pies y",pulg,"pulgadas son",totalcm,"centímetros")