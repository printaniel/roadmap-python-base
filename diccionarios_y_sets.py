"""✅ Qué debes practicar
Crear, acceder, modificar y eliminar claves en diccionarios

Recorrer con .items(), .keys(), .values()

Crear sets, operaciones de conjuntos (union, intersection, difference)

💪 Ejercicios
1. Crea un diccionario con datos de una persona: nombre, edad, país. Modifica la edad y elimina el país.

2. Recorre un diccionario de frutas y precios. Muestra cada fruta con su precio formateado: “🍌 Banana cuesta 12 CUP”.

3. Dado un texto, cuenta cuántas veces aparece cada palabra. Usa un diccionario.

4. Crea dos sets con los cursos que ofrece la CUJAE y los que ofrece otra universidad. Muestra los cursos comunes.

5. Elimina duplicados de una lista de enteros usando un set, luego vuelve a convertirlo en lista ordenada."""

# 1.
datos = {"nombre": "Aniel","edad": 20, "pais": "Cuba" }

datos["edad"] = 21
datos.pop("edad", False)
print(datos)

# 2.
tienda = {"Banana": 12, "Aguacate": 30, "Manzana": 10, "Frutabomba": 50}

def mostrar_info(diccionario):
    for fruta, precio in diccionario.items():
        print(f"{fruta} cuesta {precio} CUP")

mostrar_info(tienda)

# 3. 
texto = "¿Quieres un ejemplo aplicado al mundo real? Por ejemplo, eliminar un producto de un carrito de compras o quitar un usuario de una base de datos en memoria. Si te interesa, te lo armo. ¿Te gustaría?"
texto_dividido = texto.split(" ")
palabras = {}

for i in texto_dividido:
    if i in palabras:
      palabras[i] +=1
    else:
        palabras[i]= 1
    
print(palabras)


# 4. 

lista_enteros = [5,7, 2,3,4,5, 10,100,100,2 ,88]
lista_enteros = list(set(lista_enteros))
lista_enteros.sort()
print(lista_enteros)



        
        