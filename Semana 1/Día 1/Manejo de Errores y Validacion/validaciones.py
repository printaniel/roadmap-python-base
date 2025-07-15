"""✅ Qué practicar:
Lanzar errores propios con raise

Usar condiciones para validar entradas

Tipos de errores: ValueError, TypeError, AssertionError

💪 Ejercicios:
1. Crea una función dividir(a, b) que:
Lance un ValueError si b es cero
Devuelva el resultado en caso contrario

2. Crea una función set_edad(edad) que:
Lance un TypeError si no es un número
Lance un ValueError si es negativo
Devuelva la edad si todo está bien

3. Crea una función crear_usuario(nombre, correo) que valide:
Que el nombre tenga al menos 3 letras
Que el correo contenga "@"
Lance ValueError si no se cumple"""

def dividir(a, b):
    numero = None
    try:
        numero = a/b
    except ZeroDivisionError:
        print("La division por 0 no está definida")
    except Exception: 
        print("Solo se aceptan números")
    else:
        print("La división se llevo a cabo correctamente")        
        
    finally:
        print("Fin del programa")
    return numero


def set_edad(edad):
    if not isinstance(edad, int) or isinstance(edad, bool):
        raise TypeError("Solo se aceptan numeros enteros ")
    elif edad < 0:
        raise ValueError("La edad no puede ser negativa")       
    else:
        return edad
    
        
def crear_usuario(nombre, correo):
    
    if(len(nombre) < 3 or "@" not in correo):
        raise ValueError("Usuario o correo incorrecto")
    else:
        print("Usuario y correo correctos")
    
        
        
        



