
"""Conceptos clave:

if, elif, else

Comparadores

Operadores lógicos: and, or, not

Ejercicios:

Crea un sistema que verifique si una persona puede votar según su edad.

Crea un sistema de inicio de sesión donde el usuario y la contraseña estén hardcodeados. Si coinciden, muestra "Acceso concedido".

Verifica si un número es divisible entre 3 y 5 a la vez.

Pide tres números al usuario y muestra cuál es el mayor."""

edad = int(input("Escriba la edad de la persona: "))

if(edad >= 18 ):
    print("La persona puede votar")
else:
    print("La persona no puede votar")


usuario = "Admin"
contraseña = "Croqueta1234"
print("\n======================\n")
print("--- Login ---")
usuarioEntrante = input("Usuario: ")
contraseñaEntrante = input("Contraseña: ")

if(usuarioEntrante == usuario and contraseñaEntrante == contraseña):
    print("Acceso concedido")

else:
    print("Usuario o contraseña incorrectos") 
    
print("\n======================\n")

numero = float(input("Imprima un número: "))

if(numero % 3 == 0 and numero % 5 == 0):
    print(f"El número {numero} es divisible entre 3 y 5 a la vez")
else:
    print(f"El número {numero} no es divisible entre 3 y 5 a la vez")
    
print("\n======================\n")

numero_1 = float(input("Escriba el primer numero: "))
numero_2 = float(input("Escriba el segundo numero: "))
numero_3 = float(input("Escriba el tercer numero: "))

if(numero_1 > numero_2 and numero_1 > numero_3):
    print(f"El número mayor es {numero_1}")
else:
    if(numero_2 == numero_3 and numero_2 != numero_1):
        print(f"El número {numero_2} y {numero_3 } son los mayores")
    elif(numero_2 > numero_3):
        if(numero_2 == numero_1): 
            print(f"El número {numero_1} y {numero_2 } son los mayores")
        else:
            print(f"El número mayor es {numero_2}")
    elif(numero_3 > numero_2):
        if(numero_3 == numero_1): 
            print(f"El número {numero_1} y {numero_3 } son los mayores")
        else:
            print(f"El número mayor es {numero_3}")
    else: 
        print("Los tres numeros son iguales")
        


