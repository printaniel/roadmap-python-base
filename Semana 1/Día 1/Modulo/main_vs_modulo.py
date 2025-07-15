"""✅ Qué practicar:
Saber cuándo se ejecuta un archivo como script y cuándo como módulo

Aislar bloques de ejecución directa

💪 Ejercicios:
Crea una función saludo() que imprima "Hola desde el módulo".

Usa esta función dentro de un bloque:
if __name__ == "__main__":
    saludo()
Luego crea un archivo runner.py que importe saludo() desde main_vs_modulo.py y ejecútalo. 
Verifica que NO se imprime el saludo dos veces."""

def saludo():
    print("Hola desde el modulo")
    
if __name__ == "__main__":
    print("Prueba de la funcion de saludar desde el modulo")
    saludo()




