"""✅ Qué practicar:
Validar resultados esperados

Cubrir casos normales y casos límite

Preparar funciones para ser testeadas desde main

💪 Ejercicios:
1. Escribe una función suma(a, b) y crea al menos 3 tests con assert (suma positiva, negativa, cero).

2. Escribe una función es_par(n) que devuelva True si es par, False si no. Crea 3 tests.

3. Escribe una función formatear_nombre(nombre) que:
Devuelva el nombre capitalizado

Test: si ingreso "aniel", debe devolver "Aniel"

Simula una prueba que falle a propósito para practicar detectar fallos con assert.
"""

def suma(a,b):
    return a + b

def test_suma():
    assert suma(4,5) == 9
    assert suma(-3,-3) == -6
    assert suma(-5,4)== -1
    assert suma(0,0)== 0
    
test_suma()

def funcion_par(numero):
    return numero%2 == 0

def test_funcion_par():
    assert funcion_par(2) == True
    assert funcion_par(5) == False
    assert funcion_par(-8) == True
    
test_funcion_par()

def formatear_nombre(nombre): 
    return nombre.capitalize()

def test_formatear_nombre():
    assert formatear_nombre("aniel") == "aniel"
    assert formatear_nombre("Samantha") == "Samatha"

test_formatear_nombre()

