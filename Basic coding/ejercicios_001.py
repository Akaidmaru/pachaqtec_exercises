# Ejercicio 1 
print("Hello world.")

# Ejercicio 2
num1 = 5
num2 = 6

print("La Suma de ", num1, "+" ,num2, "es: ", num1 + num2)

# Ejercicio 3
precio_producto = 100
igv =  0.18
precio_igv = precio_producto * igv
precio_final = precio_producto + precio_igv

print("El precio del producto es: ", precio_producto)
print("El IGV es: ", precio_igv)
print("El precio final: ", precio_final, ".\n")

# Ejercicio 4

a = 15
b = 15

if a > b:
    print("El número ", a, " es mayor al número ", b, "\n")
elif b > a:
    print("El número ", b, " es mayor al número ", a, "\n")
else:
    print("Los números son iguales.")

# Ejercicio 5 y Ejercicio 6

x = 31

if x >= 0 and x <= 10:
    print("El número ", x, " es mayor o igual que 0 y menor o igual que 10.\n")
elif x >= 11 and x <= 20:
    print("El número ", x, " es mayor o igual que 11 y menor o igual que 10.\n")
elif x >= 21 and x <= 30:
    print("El número ", x, " es mayor o igual que 21 y menor o igual que 30.\n")
else:
    print("Tu número está fuera de los parámetros ingresados.")
