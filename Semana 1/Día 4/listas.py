""" Listas
Crear una lista de enteros del 1 al 10.

Eliminar todos los números pares.

Insertar el número 99 en la posición 2.

Ordenar la lista de forma descendente.

Contar cuántas veces aparece el número 5."""
lista = list(range(1,11))
lista = [i for i in lista if i % 2 != 0]
lista.insert(1,99)
lista.sort()
lista.reverse()

# Contar cuentas veces aparece el numero 5
cantidad_de_cinco = 0
for i in lista:
    if i == 5:
        cantidad_de_cinco += 1
print(lista)
print(f"Cantidad de veces que aparece el 5: {cantidad_de_cinco} ")