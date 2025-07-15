"""Ejercicios que mezclan todo
1. Crea una lista de diccionarios, donde cada diccionario representa un estudiante (nombre, nota). Recorre la lista y muestra solo los que tienen nota mayor a 90.

2. Dado un string, convierte las palabras en una lista. Luego crea un diccionario donde la clave es la palabra y el valor es su longitud.

3. Dado un conjunto con nombres duplicados (mezcla upper/lower), normaliza (todo lowercase) y elimina duplicados.

4. De una lista de tuplas (producto, precio), filtra solo los productos que valen más de 100."""

# 1. 
informacion_estudiantes = [{"Nombre": "Aniel", "Nota": 88},{"Nombre": "Liset", "Nota": 99},{"Nombre": "Raul",
                           "Nota": 92},{"Nombre": "Samantha", "Nota": 72}]

for i in informacion_estudiantes:
    informacion_estudiante= i
    if(informacion_estudiante["Nota"] > 90):
            nombre = informacion_estudiante["Nombre"]
            nota = informacion_estudiante["Nota"]
            print(f"Nombre: {nombre}, Nota: {nota}")
 
# 2. 

texto = "Hola Programador como va ese codigo"   
lista_texto = texto.split()   
diccionaro_palabras_info={}   

for i in lista_texto:
    diccionaro_palabras_info[i] = len(i)
      
print(diccionaro_palabras_info)

# 3.

nombres = ["Pedro", "Aniel", "Raul", "Mouredev", "Mouredev"]
nombres = list(set(nombres))
nombres = [nombre.lower() for nombre in nombres]
print(nombres)

# 4.

lista_productos = [("Mouse", 10),("Mouse Gamer", 30), ("TV", 180), ("Aire Acondicionado",300)]

lista_productos = [producto for producto in lista_productos if producto[1] > 100]
print(lista_productos)

    