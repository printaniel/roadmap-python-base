
def suma(a, b):
    numeros = validar_numeros(a,b)        
    return sum(numeros)
    
    
def resta(a, b):
    numeros = validar_numeros(a,b)
    
    return numeros[0] - numeros[1]

def multplicacion(a, b):
   numeros = validar_numeros(a,b)
   return numeros[0] * numeros[1]
 
def division(a,b):
    numeros = validar_numeros(a,b)
    if numeros[1] == 0:
        raise ZeroDivisionError("La division por 0 no esta definida")
    else:
        return numeros[0] / numeros[1]
 
    
    
def validar_numeros(*args): 
   
   son_validos = True
   contador = 0
   numeros = []
   
   for i in args:
    
       try:
           numero = float(i)
           numeros.append(numero)
       except:
           son_validos = False
           raise ValueError("Solo se aceptan números")
   
   return numeros
    
def pedir_numero():
    return input("Escriba un numero: ")