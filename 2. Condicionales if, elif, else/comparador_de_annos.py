"""
Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han
pasado desde ese año o cuántos años faltan para llegar a ese año.
"""

print("==================")
print("COMPARADOR DE AÑOS")
print("==================")

actual = int(input("¿En qué año estamos?: "))
otro = int(input("Escriba un año cualquiera: "))

if actual < otro:
	print (f"Para llegar a {otro}, faltan {otro - actual} años.")
elif actual > otro:
	print (f"Han pasado {actual - otro}, desde el año {otro}. ")
else:
	print("¡Son el mismo año!")






