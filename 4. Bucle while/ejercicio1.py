"""
Crear un programa que permita al usuario procesar los montos de las compras de un cliente 
se desconoce la cantidad de datos que cargara), cortando el ingreso de datos cuando ingrese el monto 0. 
Si ingresa un monto negativo, no se debe procesar y se debe pedir que proporcione un nuevo monto.
Al finalizar, informar el total a pagar teniendo en cuenta que, si las ventas superan el total de $1000,
se le debe aplicar un 10% de descuento.
"""
total = 0

monto = float(input("Ingrese el monto de la compra: "))
while monto != 0:
	if monto < 0:
		print("Monto no valido")
	else:
		total = total + monto
		monto = float(input("Ingrese nuevo monto de la compra: "))

if total >= 1000:
	descuento = (total*10)/100
	total = total - descuento

print()

print(f"El monto total a pagar es: {total}")