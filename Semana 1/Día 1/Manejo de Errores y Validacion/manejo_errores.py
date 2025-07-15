"""✅ Qué practicar:
try, except, else, finally

Captura de errores específicos: ValueError, ZeroDivisionError, IndexError

Varios except, encadenados

💪 Ejercicios (enunciados):
1. Crea un programa que pida dos números al usuario y los divida. Captura si el segundo es cero y muestra “No se puede dividir entre cero”.

2. Pide un número al usuario y conviértelo a entero. Si no se puede, muestra un mensaje de error personalizado.

3. Crea una lista con 5 elementos. Pide un índice al usuario y muestra el elemento correspondiente. Si el índice está fuera de rango, informa con un mensaje.

4. Usa else y finally para mostrar:

“La operación fue exitosa” solo si no hubo excepción

“Fin del programa” pase lo que pase"""

# 1.

numero_1 = float(input("Escriba el primer número: "))
numero_2 = float(input("Escriba el segundo número: "))

def dividir_numeros(numero1, numero2):
    total = None
    try:
        total = numero1/numero2
    except ZeroDivisionError :
        print("No se puede dividir entre 0")
    else:
        print("Operación exitosa")  
    finally:
        print("Fin del programa")
    return total

print(dividir_numeros(numero_1,numero_2))

# 2.

def pedir_entero():
    numero = None
    try:
        numero = int(input("Escriba un numero entero: "))
    except:
        print("Solo se aceptan números enteros")
    else:
        print("Número recibido")
    finally:
        print("Fin del programa")
    
    return numero

pedir_entero()

# 3.


lista = [3,4,5,6,7]

def pedir_indice(lista):
    
    elemento =  None
    try:
        numero = int(input("Escriba la posición a la que quiere acceder: "))
        
        if(numero <= 0 ):
            raise IndexError
        
        elemento = lista[numero-1]
        
    except ValueError: 
        print("Solo se aceptan números enteros ")
    except IndexError:
        print("Indice fuera de rango")
        
    else:
        print("Has accedido al elemento correctamente")        
    finally:
        print("El programa ha finalizado")
    
    return elemento

pedir_indice(lista)