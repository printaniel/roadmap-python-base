"""En geometria.py: funciones para calcular área y perímetro de:

Cuadrado

Rectángulo

Triángulo
"""

# Cuadrado

from . import aritmetica
import math

def perimetro_cuadrado(a):
    numeros = aritmetica.validar_numeros(a)
    return numeros[0]*4
           
def area_cuadrado(a):
    numeros = aritmetica.validar_numeros(a)
    return numeros[0]**2


# Rectangulo
def perimetro_rectangulo(a,b):
    numeros = aritmetica.validar_numeros(a,b)
    return 2*(numeros[0] + numeros[1])
    
def area_rectangulo(a,b):
    numeros = aritmetica.validar_numeros(a,b)
    return numeros[0] * numeros[1]


# Triangulo
def perimetro_triangulo(a,b,c):
    numeros = aritmetica.validar_numeros(a,b,c) 
    if verificar_desigualdad_triangular(numeros[0],numeros[1],numeros[2]):
        return numeros[0] + numeros[1] + numeros[2]
    
def area_triangulo(a,b,c):
    numeros = aritmetica.validar_numeros(a,b,c)
    if verificar_desigualdad_triangular(numeros[0],numeros[1],numeros[2]):
        
        semiperimetro = perimetro_triangulo(numeros[0],numeros[1],numeros[2])/2 
        area = math.sqrt(semiperimetro * (semiperimetro - numeros[0]) * (semiperimetro - numeros[1]) * (semiperimetro - numeros[2]))
        return area
        

def verificar_desigualdad_triangular(a,b,c):
    valido = False
    if  a + b > c and  a + c  > b and  b + c > a:
        valido = True
    else:
        raise ValueError("No se cumple la desigualdad triangular")
    
    return valido

