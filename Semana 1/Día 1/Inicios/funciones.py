"""Conceptos clave:

def, return

Argumentos por defecto

*args, **kwargs

Alcance (global, nonlocal)

Ejercicios:

Crea una función que reciba un nombre y devuelva un saludo.

Crea una función suma_total que reciba cualquier cantidad de números y
devuelva su suma total usando *args.

Crea una función que reciba datos personales como nombre, edad, país, etc., y
los imprima uno por uno con **kwargs.

Crea una función anidada que incremente una variable local (nonlocal) cada vez que se llama.

Usa global para modificar una variable externa desde una función 
(solo con fines de práctica, no es buena práctica real)."""

def saludar(nombre):
    print(f"Holaaa {nombre}!!")
    
saludar("Aniel")

def suma_total(*args):
    total = 0
    for i in args:
        total += i
    return total

def mostrar_info(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave}:{valor}")

print(suma_total(*[3,4,3]))
mostrar_info(Nombre = "Aniel", edad = 20, estatura = 1.71)


def mi_contador():
    cuenta = 0
    def incremeto():
         nonlocal cuenta
         cuenta += 1
         
         return cuenta
    
    return incremeto

mi_contador = mi_contador()  # crea una nueva "instancia" del contador

print(mi_contador())  # 1
print(mi_contador())  # 2
print(mi_contador())  # 3


nombre = "Aniel"

def modificar_nombre():
    global nombre 
    nombre = "Raul"
    
print(nombre)
modificar_nombre()
print(nombre)
    



    



