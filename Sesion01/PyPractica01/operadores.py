print("Operadores en Python")
print("-" * 25)

print(18 + 4)

numero1 = 10
numero2 = 5

print("Suma:", numero1 + numero2)
print(numero1 / numero2)
print(numero1 // numero2)
print(numero1 % numero2)

numero3 = 2
print(numero3 ** 5)

print("Operadores de comparación")
print("-" * 25)
print(numero1 == numero2)
print(numero1 == "30")
print(numero1 == 30)

print(numero1 != numero2)
print(numero1 > numero2)
print(numero1 < numero2)
print(numero1 >= numero2)
print(numero1 <= numero2)

print("Operadores lógicos")
print("-" * 25)
print(numero1 and numero2)
print(numero1 or numero2)
print(not numero1)

print("True and True: ", True and True)
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)

# Los alumnos mayores de 15 años y que tienen
# la ficha llenada pueden usar la piscina
edad_alumno = 16
ficha_llenada = True
edad_necesaria = edad_alumno >= 15
puede_usar_piscina = edad_necesaria and ficha_llenada
print("¿Puede usar la piscina?", puede_usar_piscina)

print("True or True: ", True or True)
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)

# email debe ser unico

correo_registrado = True
print(not correo_registrado)

correo_registrado = False
print(not correo_registrado)


