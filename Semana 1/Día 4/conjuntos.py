"""Conjuntos
Crear un conjunto con las vocales de una palabra.

Comparar con otro conjunto de vocales de otra palabra.

Mostrar vocales en común, y las vocales diferentes.

"""
vocales_list = ["a","e","i","o","u"]
palabra1 = "murcielago"
palabra2 = "aaaaaaaa"
            
def buscar_vocales(palabra, vocales):
    vocales_palabra = set()
    for i in palabra:
        if i in vocales:
            print(i)
            vocales_palabra.add(i)
            
    return vocales_palabra

lista_vocales1 = buscar_vocales(palabra1, vocales_list)
lista_vocales2 = buscar_vocales(palabra2,vocales_list)

print(lista_vocales1)
print(lista_vocales2)

def buscar_comunes(lista, lista2):
    comunes = set()
    for i in lista:
        if i in lista2:
            comunes.add(i)
    return comunes
    
def buscar_no_comunes(lista,lista2):
    no_comunes = set()
    for i in lista:
        if not i in lista2:
           no_comunes.add(i)
    return no_comunes

print(f"Las vocales comunes en las dos listas son :{buscar_comunes(lista_vocales1,lista_vocales2)}")
print(f"Las vocales no comunes en las dos listas son:{buscar_no_comunes(lista_vocales1,lista_vocales2)}")