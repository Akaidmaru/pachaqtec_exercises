# Tupla Meses
months = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre' )

while True:  
    ans = int(input('Inserta un número, ingresa 0 para salir: '))
    if ans == 0:
        break
    elif ans >= 1 and ans <= len(months) + 1:
        print(months[ans-1])
    else:
        print('Necesitas seleccionar un número del 1 al 12 para saber el mes.')

# Cuenta repeticiones en tupla.

nums = (1, 1, 2, 0, 3, 4, 8, 8, 7, 7, 5, 6, 6, 5, 5, 5, 9, 3, 2, 1, 8, 1, 1, 2, 0, 3, 4, 8, 8, 7, 7, 5, 6, 6, 5, 5, 5, 9, 3, 2, 1, 8, 1, 1, 2, 0, 3, 4, 8, 8, 7, 7, 5, 6, 6, 5, 5, 5, 9, 3, 2, 1, 8, 1)

ans_2 = int(input('Ingresa un numero para saber cuantas veces está repetido en la tupla: '))

print('El número', ans_2, 'aparece', nums.count(ans_2), 'veces.')
