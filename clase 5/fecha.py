
from datetime import datetime, date, time, timedelta


print(datetime(2023,9,18) )

print(date(2023,9,18) )

print(time(23,9,18) )


print("datetime now",datetime.now() )

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") )

print(datetime.now().strftime("%d-%Y-%m") )

print( isinstance(datetime.now().strftime("%d-%Y-%m"), str) )

print( datetime.today() )

print( date.today().weekday() )

import locale   


print(date.today().strftime("Hoy es %A del mes %B"))

print( locale.getlocale() )
locale.setlocale(locale.LC_ALL, "es") #para ver las cadenas en español, en argentina es_AR pero no me lo toma

print(date.today().strftime("Hoy es %A del mes %B"))

fecha_cadena="18/9-2023"
fecha=datetime.strptime(fecha_cadena, "%d/%m-%Y")
print(fecha)
print(fecha.strftime("la fecha es: %d-%m-%Y , y la hora: %X"))


intervalo_tres_dias=timedelta(3)
fecha_en_tres_dias=datetime.now()+intervalo_tres_dias
print(fecha_en_tres_dias.strftime("%d-%m-%Y") )

mi_nacimiento= "16/12/1995" #date(1995,12,16)
periodo=date.today()- datetime.strptime(mi_nacimiento,"%d/%m/%Y").date() #.strftime("%Y/%m/%d") #mi_nacimiento
print(periodo.days)

mi_edad=periodo.days//365
print(f"{mi_edad} años")
print(datetime.strptime(mi_nacimiento,"%d/%m/%Y").date())
print(date.today())