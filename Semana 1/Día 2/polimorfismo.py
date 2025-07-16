"""✅ Qué practicar:

Métodos con el mismo nombre en diferentes clases

Uso de una misma interfaz para múltiples tipos de objetos

💪 Ejercicios (sin respuestas):

Crea tres clases: Perro, Gato, y Pajaro, cada una con un método hacer_sonido() que imprima un sonido distinto.

Crea una función reproducir_sonido(animal) que reciba cualquier objeto y llame a su hacer_sonido().

Agrega un método moverse() en cada clase que haga algo diferente.

Usa un bucle para recorrer una lista con diferentes animales y llamar sus métodos."""
from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @abstractmethod
    def moverse(self):
        pass


class Perro(Animal):
    
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        print("Guau Guau!!")
        
    def moverse(self):
        print("Se mueve rapido")
        
class Gato(Animal):
    
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        print("Miau Miau!!")
    
    def moverse(self):
        print("Se mueve muy rapido")
        
class Pajaro(Animal):
    
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        print("Grrr Grrr!!")
    
    def moverse(self):
        print("Vuela")
        

   
  # Crear animales
perro1 = Perro("Firulais")
gato1 = Gato("Michi")
pajaro1 = Pajaro("Piolín")
perro2 = Perro("Rocky")
gato2 = Gato("Garfield")

# Guardar algunos en una lista
animales = [perro1, pajaro1, gato2] 
    
def reproducir_animal(animal):
    animal.hacer_sonido()
    
def mover_animal(animal):
    animal.moverse()
    
def reproducir_animales(lista_animales):
    
    for i in lista_animales:
        i.hacer_sonido()

reproducir_animal(pajaro1)

mover_animal(gato2)

reproducir_animales(animales)