"""✅ Qué practicar:

Método constructor __init__()

Inicializar atributos al crear objetos

💪 Ejercicios:

Crea una clase Auto que reciba marca, modelo y año al crearse.

Agrega un método descripcion() que devuelva: "Toyota Corolla 2020".

Crea una lista con varios autos distintos y muestra sus descripciones.

Agrega un atributo encendido por defecto en False y un método encender()."""

class Auto:
    
    encendido = False
    
    def __init__(self,marca,modelo,annioCreacion):
        self.marca = marca
        self.modelo = modelo
        self.annioCreacion = annioCreacion
        
        
    def descripcion(self):
        print(f"{self.marca} {self.modelo} {self.annioCreacion}")
        
    def encender(self):
        self.encendido = True
        
        
auto_1 = Auto("Toyota", "Corolla" ,2020)
auto_2 = Auto("Chevrolet","Camaro",2001)

auto_1.descripcion()
auto_2.descripcion()
auto_1.encender()
        
        
        
