try:
    edad = input("Ingrese su edad: ")
    edad = int(edad)  # Convertir la entrada a un número entero
    print(f"Su edad es: {edad}")
    print(f"En 10 años tendrá: {edad + 10}")
except ValueError:
    print("Por favor, ingrese un número válido para la edad.")
finally:
    print("Gracias por usar el programa.")