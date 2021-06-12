# tupla mayor y menor 
nums = (1, 1, 2, 0, 3, 4, 8, 8, 7, 7, 5, 6, 6, 5, 5, 5, 9, 3, 2, 1, 8, 32, 1, 2, 25, 3, 4, 30, 8, 7, 7, 5, 6, 6, 5, 5, 5, 9, 3, 2, -1, 8, 1, 1, 2, 0, 3, 4, 8, 51, 7, 7, 5, 6, 6, 5, 5, -5, 9, 3, 2, 1, 8, 1, 15)

print('El número menor en la tupla es:', min(nums))
print('El número mayor en la tupla es:', max(nums))


# dict nombre de usuario y valor sea teléfono. Tedra que ir pidiendo contactos hasta que el usuario no quiera más, no se pueden meter nombres repetidos.

contacts = {}
while True:
    contact = input('Ingresa el nombre de un contacto que quieras guardar, ingresa "q" para salir: ')
    if contact.lower() == 'q':
        break
    elif contact in contacts:
        print('Ya ese contacto existe, intenta con otro.')
    else:
        phone_num = input('Ingresa un número de teléfono para registrarlo: ')
        contacts[contact] = phone_num      

print(contacts)