def hola():
    print("Hola, ¿cómo estás?")
def saludar(nombre, saludo):
    return f"{saludo}, {nombre}"
hola()
mensaje = saludar("Frank", "Buenas noches")
print(mensaje)

x = 5

def suma():
    y = 10
    return x + y
print(suma())

print("-" * 25,"Type hints")

def area(base: int, altura: int) -> int:
    return base * altura
print(area(5, 10))
print(area(5.8, 10))
print(area("Hola ", 6))