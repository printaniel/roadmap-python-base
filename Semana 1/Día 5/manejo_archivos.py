"""Crear un archivo agenda.txt con nombres y teléfonos. Leerlo línea por línea.

Crear una función que escriba el log de ejecución de tu script en un archivo log.txt.

Escribir una función que lea un archivo .txt y cuente la cantidad de palabras.

Crear un programa que lea un archivo .csv con notas de estudiantes y calcule el promedio.

Leer un archivo línea por línea y escribir solo las líneas que contengan una palabra clave en otro archivo."""


def leer_archivo(archivo):

    with open(archivo,"r",encoding = "utf-8") as arch:
        contenido = arch.read()
    return contenido

def contar_palabras(archivo):
    palabras = palabras.split(" ")    
    return len(palabras)

def calcular_promedio_estudiantes(archivo_csv):
    with open(archivo_csv,"r",encoding="utf-8") as archivo:
                
        total = 0
        cantidad_estudiantes = 0
        
        for linea in archivo:
            cantidad_estudiantes += 1
            notas = linea.split(",")
            notas = [int(i.strip()) for i in notas if i.strip().isdigit()]
            total = sum(notas)
                    
            
    return total/cantidad_estudiantes

print(calcular_promedio_estudiantes("notas.csv"))

def buscar_info_importante(archivo,archivo_guardar,palabra):
    
    with open(archivo,"r",encoding="utf-8") as arch:
        for i in arch:
            if palabra in i:
                with open(archivo_guardar,"a",encoding="utf-8") as arch1:
                    arch1.write(i)

buscar_info_importante("info.txt","info_importante.txt", "Python")

                    
        

