# Evaluar nota de un alumno
# 1. Pedir nota del alumno
# 2. Dar mensaje de evaluacion 

nota = int(input("Ingrese la nota del alumno: "))

if nota <= 11:
    print("El alumno está desaprobado.")

if 12 <= nota <= 14:
    print("Necesita un examen de recuperación.")
print("No estoy dentro de la condicional")

print("-" * 10, "Metodo 2", "-" * 10)
if nota <= 11:
    print("El alumno está desaprobado.")
elif nota <= 14:
    print("Necesita un examen de recuperación.")
elif nota <= 19:
    print("El alumno está aprobado.")
elif nota == 20:
    print("Aprobaste con una nota sobresaliente, felicidades.")
else:
    print("La nota ingresada no es válida.")


