"""✅ Qué debes practicar
Indexado, slicing, append, extend, insert, remove, pop, reverse, sort

Inmutabilidad de las tuplas

Desempaquetado

💪 Ejercicios 
1. Crea una lista con 5 nombres. Añade uno más al final. Inserta otro en la segunda posición. Luego elimínalo por nombre.

2. Invierte una lista sin usar reverse() ni slicing. Hazlo con un bucle.

3. Dada la tupla (3, 5, 7), convierte a lista, añade un número, vuelve a convertirla en tupla.

4. Usa slicing para obtener los 3 últimos elementos de una lista de 7 números.

5. Usa desempaquetado para asignar los valores de una tupla (10, 20, 30) a tres variables y súmalas."""

# 1.
nombres = ["Aniel","Raul","Lazaro", "Amanda", "Maloy"]
nombres.append("Liset")
nombres.insert(1,"Jenifer")
nombres.remove("Jenifer")
print("Lista Actual")
print(nombres)

# 2. 
def invertir_lista(lista):
    
    nueva_lista = []
    for i in nombres[::-1]:
            nueva_lista.append(i)
            
    lista [:] = nueva_lista

print("Lista antes del cambio")
print(nombres)
print("Lista despues del cambio")
invertir_lista(nombres)
print(nombres)
    
# 3.

numeros = (3, 5, 7) 
numeros = list(numeros)
numeros.append(9)
numeros = tuple(numeros)

print(numeros)

# 4. 
lista = [5,6,7,2,2,3,4]

print(lista[4::])

# 5.  Usa desempaquetado para asignar los valores de una tupla (10, 20, 30) a tres variables y súmalas.
tupla = (10, 20, 30)

num_1,num_2,num_3 = tupla[0],tupla[1], tupla[2]

print(num_1)
print(num_2)
print(num_3)
        




