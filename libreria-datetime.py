import datetime
import time
separador = ("°°°" * 40) + "\n"

# Hora
hora = datetime.time(10,20,30,40)
print(f" El tipo de objeto de la hora es: {type(hora)}")
print(f" La hora que se marca es: {hora}")
print(f" La hora es: {hora.hour}")
print(f" El minuto es: {hora.minute}")
print(f" El segundo es: {hora.second}")
print(f" El microsegundo es: {hora.microsecond}")
print (separador)

# Fecha Actual
fecha_actual = datetime.date.today()
print(f" El tipo de objeto de la fecha es: {type(fecha_actual)}")
print(f" La fecha actual es: {fecha_actual}")
print(f" El año actual es: {fecha_actual.year}")
print(f" El mes actual es: {fecha_actual.month}")
print(f" El dia actual es: {fecha_actual.day}")
print (separador)

# Fecha Capturada
fecha_capturada = input("Dime una fecha con el formato dd/mm/aaaa: \n")
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()
print(type(fecha_capturada))
print(type(fecha_procesada))
print(f"La fecha capturada se transforma a {fecha_procesada}")
print (separador)

# Sumandole dias a la fecha
cant_dias=int(input("Dime la cantidad de dias a adelantar: \n"))
nueva_fecha = fecha_procesada + datetime.timedelta(days= + cant_dias)
print(f"La nueva fecha es {nueva_fecha}")
