"""
CONCEPTOS CLAVES:

Variables (nombre = "Aniel")

Tipos (int, float, str, bool)

type(), isinstance()

input(), conversiones

EJERCICIOS:

Declara una variable con tu nombre, otra con tu edad y otra con tu estatura. Imprime todo en una sola línea usando f-string.

Pide al usuario que introduzca un número, y muestra su doble. Asegúrate de convertirlo al tipo correcto.

Verifica si una variable es tipo float usando isinstance().

Crea una variable llamada activo de tipo bool y muestra su valor negado usando not.
"""

nombre = "Aniel"
edad = 20
estatura = 1.71
activo = True


print(f"Mi nombre es {nombre}, tengo {edad} años y mi estatura es {estatura} cm")

print(f"El nombre es de tipo: {type(nombre)}")
print(f"La edad es de tipo: {type(edad)}")
print(f"La estatura es de tipo: {type(estatura)}")

numero = float(input("Escriba un número: "))
print(f"El doble del número {numero} es: {numero * 2}")

print(f"El numero es de tipo float: {isinstance(numero,float)}")

print(f"Valor actual de la variable activo: {activo} \nValor contrario de la variable activo: {not activo}")








