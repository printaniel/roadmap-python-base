"""✅ Qué practicar:

Aplicar todos los conceptos anteriores

💪 Ejercicios:

Crea una clase Producto con nombre, precio y stock. Agrega método vender() que baje el stock.

Crea una clase Estudiante con nombre y lista de notas. Agrega método promedio().

Crea un pequeño sistema donde puedas guardar varios estudiantes y mostrar su promedio."""
class Producto:

    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def vender(self, cantExtraer):
        self.stock -= cantExtraer
        
    
class Estudiante:
    
    def __init__(self, nombre, listaNotas):
        self.nombre = nombre
        self.listaNotas = listaNotas
        
    def promedio(self):
        return sum(self.listaNotas)/len(self.listaNotas)
    


class Escuela:
    
    def __init__(self):
        self.estudiantes = []
    
    def agregarEstudiante(self, nombre, listaNotas):
        self.estudiantes.append(Estudiante(nombre,listaNotas))
