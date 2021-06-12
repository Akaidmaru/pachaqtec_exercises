#! /usr/bin/env

from datetime import date, datetime
from datetime import timedelta

today = date.today()
now = datetime.now()

# print(today)
# print("El día actual es {}".format(today.day))
# print("El mes actual es {}".format(today.month))
# print("El a#o actual es {}".format(today.year))

# print(now)

# print("El día actual es {}".format(now.day))
# print("El mes actual es {}".format(now.month))
# print("El a#o actual es {}".format(now.year))

# print("La hora actual es {}".format(now.hour))
# print("Los minutos actuales son {}".format(now.minute))
# print("Los segundos actuales son {}".format(now.second))
# print("Los microsegundos actuales son {}".format(now.microsecond))

new_date = datetime(2016, 9, 29, 10, 15, 00, 00000) #a#no, mes, dia, hora
# minuto, segundo, microsegundo

# print(new_date)

final_delta = new_date + timedelta(days=365)

# print(final_delta)

# print(type(today))

print(final_delta.strftime('%d/%b/%Y'))
print(final_delta.strftime('%d/%m/%Y - %H:%M:%S'))
print(final_delta.strftime('La fecha de hoy es %d/%b/%Y, a las %H:%M:%S'))


