from random import *

secret_number = randint(1, 100)
tries = 0

while True:
    guess = input('Ingresa un número del 1 al 100. Trata de describir el número secreto: ')
    tries += 1
    if int(guess) == secret_number:
        print('¡Bien hecho!, ¡Has encontrado el número secreto!')
        print('Te ha tomado: ' + str(tries) + ' intento(s).')
        break
    elif int(guess) > secret_number:
        print("¡Tu número es mayor que el número secreto!")
    else:
        print("¡Tu número es menor que el número secreto!")