"""✅ Qué practicar:

Definición de una clase

Crear objetos (instancias)

Atributos públicos

💪 Ejercicios (solo enunciados):

Crea una clase Perro con un atributo nombre y un método ladrar() que imprima "¡Guau!".

Instancia dos objetos de tipo Perro con diferentes nombres y hazlos ladrar.

Añade un atributo raza y cambia su valor luego de instanciar."""

class Perro:
   
    def __init__(self, nombre):
        self.nombre = nombre
        
    def ladrar(self):
        print("Gua Gua!")
    
        
perro_1 = Perro("Loki")
perro_2 = Perro("Pili")


perro_1.ladrar()
perro_2.ladrar()

perro_1.raza = "Rootwiller"
perro_2.raza = "Sato"

print(perro_1.raza)
print(perro_2.raza)


