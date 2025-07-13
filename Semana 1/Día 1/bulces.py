"""Conceptos clave:

for con range()

while

break, continue

Ejercicios:

Imprime los números del 1 al 10 usando un bucle for.

Usa while para pedir una contraseña hasta que el usuario escriba la correcta.

Muestra los números del 1 al 20, pero omite los múltiplos de 3 usando continue.

Recorre una lista de nombres y detén el bucle si encuentras el nombre "Aniel"."""

for i in range(1,11):
    print(i)
 
print("\n==========\n")  
 
contraseña = "Croquetas1234"
salir = False

while(salir == False):
    
    print("Escriba la contraseña (escriba salir si es lo que quiere hacer)")
    contraseñaActual = input("Contraseña: ")
    
    if(contraseñaActual == contraseña ):
        print("Contraseña correcta!!")
        salir = True
    elif(contraseñaActual == "salir"):
        salir = True
    else:
        print("Contraseña incorrecta, inténtelo de nuevo...")

print("\n==========\n") 

for i in range(1,21):
    if(i % 3 ==0):
        continue
    else:
        print(i)
        
print("\n==========\n") 

nombres = ["Raul","Samantha", "Ernesto","Aniel", "Yuran", "Adrian"]
encontrado = False

i = 0

while(i< len(nombres) and encontrado == False):
    if(nombres[i] == "Aniel"):
        print("El nombre ha sido encontrado")
        encontrado = True
    i+=1
    
    
    
    