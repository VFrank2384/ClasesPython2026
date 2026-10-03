frutas = ["manzana", "banana", "naranja", "pera", "kiwi"]
print(frutas)
print(frutas[1])  # Acceder al segundo elemento de la lista
print(frutas[-1])  # Acceder al último elemento de la lista 

frutas[2] = "mango"  # Modificar el tercer elemento de la lista
print(frutas)

frutas.append("fresa")  # Agregar un nuevo elemento al final de la lista
print(frutas)
frutas.insert(2, "uva")  # Insertar un nuevo elemento en la posición 2
print(frutas)
frutas.pop(1)  # Eliminar el último elemento de la lista
print(frutas)

eliminado = frutas.pop(1)  # Eliminar el elemento en la posición 1 y guardarlo en una variable
print(frutas, eliminado)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[::2])  # Acceder a los elementos en posiciones pares (0, 2, 4, 6, 8)
print(numeros[::3])  # Acceder a los elementos en posiciones múltiplos de 3 (0, 3, 6, 9)

numeros_2 = [11, 12, 13, 14, 15]
print(numeros_2[2])  # Acceder a los elementos desde la posición 2
print({"Peru", "Colombia", "Argentina", "Peru"})  # Crear un conjunto con tres elementos