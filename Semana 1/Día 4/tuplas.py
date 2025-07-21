"""Crear una tupla con las notas de un estudiante.

Calcular el promedio de las notas.

Mostrar la cantidad de veces que aparece la nota 10."""

tupla = (2,2,3,4,10,3,2,9,5,10)

promedio_de_notas = sum(tupla)/len(tupla)

cantidad_aparece_diez = 0

for i in tupla:
    if i == 10:
        cantidad_aparece_diez += 1

print(f"Notas del estudiante: {tupla}")
print(f"Promedio de notas: {promedio_de_notas}")
print(f"Cantidad de veces que aparece el diez: {cantidad_aparece_diez}")