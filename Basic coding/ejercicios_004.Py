# Ejercicios 12 

string_1 = input("Ingresa un primer string: ")
string_2 = input("Ingresa un segundo string: ")

print(string_2[:2] + string_1[2:] + " " + string_1[:2] + string_2[2:])

# Ejercicios 13 palíndromo

string_3 = input("Ingresa una palabra para chequear si es un palíndromo: ")

if string_3.lower().replace(" ", "") == string_3[::-1].lower().replace(" ", ""):
    print(string_3 + " es un palíndromo.")
else:
    print("No es un palíndromo.")
