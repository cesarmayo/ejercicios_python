# coding=utf-8
"""
Un instituto de ensennanza de ingles necesita un programa que le permita cada dia, procesar observaciones sobre las clases de ese dia.
El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un dia de la semana difrerente: los lunes se
dicta el nivel inicial, los martes el nivel intermedio, los miercoles el nivel avanzado, los jueves son para practica hablada y los
viernes se dicta ingles para viajeros.

Se debe comenzar por solicitar al ususario la fecha actual en formato "dia, DD/MM, donde "dia" es un dia de la semana, "DD" es el numero
de dia con rrspecto al mes y "MM" es el numero de mes con respecto al año.

Si el usuario ingresa un dia de la semana inexistente o una fecha cuyo dia supere el nro 31 o el mes supere el numero 12, finalizar el
programa indicando que se produjo un error.

Debe permitirse que ingrese el dia de la semana en minusculas o mayusculas indistintamente. Como condicion se tiene que lo ingresado por
el usuario tendra la forma <[alfanumerica], [numerico]/[numerico]>.

Una vez iniciada la fecha, el usuario necesita poder iniciar si ese dia se tomaron examenes, pero eso solo si se trata de los niveles
inicial intermedio o avanzado, ya que las practicas habladas y el ingles para viajeros no tienen examenes.

Si hubo examenes el usuario ingresara cuantos alumnos aprobaron y cuantos no el programa mostrara el porcentaje de aprobados.

Si el dia fue correspondiente a practica hablada el usuario debera ingresar el porcentaje de asistencia a clase y el programa indicara
"asistio la mayoria" en caso de que la asistencia sea mayor a 50% o " no asistio la mayoria" si no es asi.

Si se trata de ingles para viajeros y la fecha actual corresponde al dia 1 de mes 1 o del mes 7, se debera imprimir "comienzo del nuevo
ciclo" y solicitar al usuario que ingrese la cantidad de alumnos de nuevo ciclo y el arancel en "dolares" por cada alumno para luego
imprimir el ingreso total en dolares.
"""

date = input("Ingrese la fecha (dia, DD/MM): ")
date = date.lower()
dia_semana = date[0 : date.find(",")]
dia_mes = int(date[date.find(" ") : date.find("/")])
mes = int(date[date.find("/")+1 : ])

if dia_semana not in ("lunes martes miercoles jueves viernes") or (dia_mes > 31 or mes > 12): 
	print("Se produjo un error..!")
else:
	if dia_semana in ("lunes martes miercoles"):
		examenes = input("se tomaron examenes ese dia (S,N):")
		if(examenes=="s" or examenes=="S"):
			aprobados = int(input("Ingrese la cantidad de aprobados: "))
			reprobados = int(input("Ingrese la cantidad de reprobados: "))
			total_evaluados = (aprobados + reprobados)
			porcentaje_aprobados = (aprobados / total_evaluados) * 100
			print("El porcentaje de aprobados es:", porcentaje_aprobados,"%" )
	elif dia_semana in ("jueves"):
		porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia: "))
		if (porcentaje_asistencia > 50):
			print("Asistio la mayoria..!")
		else:
			print("No asistio la mayoria..!")
	elif dia_semana in ("viernes"):
		if ((dia_mes == 1) and (mes ==1 or mes==7)):
			print("Comienzo de nuevo ciclo..!")
			cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
			arancel = int(input("Ingrese el arancel en $: "))
			ingreso_total = (cantidad_alumnos*arancel) 
			print("El ingreso total es de:",ingreso_total)


