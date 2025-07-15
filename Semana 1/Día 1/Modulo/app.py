from calculadora import suma as s
from calculadora import divide as d
from calculadora import resta as r
from calculadora import multiplica as m
import calculadora


# Multiplicacion de dos nuemros 
print(m(4,5))

# Suma de dos numeros 
print(s(10,5))

# Resta de dos numeros 
print(r(9,9))

# Division entre dos numeros
print(d(30,2))

# Otra forma de obtener una funcion de otro archivo (multiplicacion en este caso )
print(calculadora.multiplica(4,9))
