"""
Escriba un programa que pida una cantidad y que escriba cuantas gruesas,
docenas y unidades son.
Se recuerda que una gruesa son doce docenas
"""
print("CONVERTIDOS A GRUESAS Y DOCENAS")
cantidad = int(input("Escriba una cantidad entera: "))
gruesas = cantidad//144
temp = cantidad%144
docenas = temp//12
unidades = temp%12
print(cantidad, "unidades son",gruesas, "gruesas,", docenas,"docenas y", unidades, "unidades")

    
