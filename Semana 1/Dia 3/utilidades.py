
"""Módulo utilidades.py

Crea un módulo con funciones que:

1. Devuelvan el factorial de un número

2. Comprueben si una palabra es palíndroma

3. Conviertan un número decimal a binario
"""

# 1. 
def calcular_factorial(numero):
    factorial = 0
    
    for i in range(1,numero + 1):
        factorial *= numero
        
    return factorial

# 2.

def verificar_palindroma(palabra):
    
    es_palindroma = False
    palabra = palabra.lower()
    
    palabra_lista = list(palabra)
    palabra_lista.reverse()
    palabra_revertida = ""
    
    for i in palabra_lista:
        palabra_revertida += i
    
    if palabra == palabra_revertida:
        es_palindroma = True
    
    return es_palindroma


# 3.

def convertir_a_binario(numero):
    binario = ""
    binario_revertido = []
    
    while numero > 0:
        resto = numero % 2        
        numero = numero // 2
        binario_revertido.append(str(resto))
    
    binario_revertido.reverse()
    binario = "".join(binario_revertido)
       
    return binario

# Ejemplo de uso
print(convertir_a_binario(16))
    

