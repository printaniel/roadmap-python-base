"""Qué practicar:

Crear una clase base

Crear clases hijas que extienden la base

Sobrescribir métodos (override)

Uso de super()

💪 Ejercicios (sin respuestas):

Crea una clase base Empleado con nombre y salario.

Crea una clase Gerente que herede de Empleado y añada equipo_a_cargo.

Sobrescribe un método mostrar_info() para que también muestre el equipo.

Crea otra clase Programador que agregue el lenguaje que maneja.

Usa super() para mantener la funcionalidad base en las clases hijas."""


from typing import override

class Empleado:
    
    def __init__(self,nombre,salario):
        self._nombre = nombre
        self._salario = salario
    
    def mostrar_info(self):
        print(f"Nombre:{self.nombre}, salario: {self.salario}")
    
class Gerente(Empleado):
    
    def __init__(self, nombre, salario, equipo_a_cargo):
        super().__init(nombre,salario)
        self.__equipo_a_cargo = equipo_a_cargo
        
    @property
    def __equipo_a_cargo(self):
        return self.__equipo_a_cargo
    
    @__equipo_a_cargo.setter
    def __equipo_a_cargo(self, equipo_a_cargo):
        self.__equipo_a_cargo = equipo_a_cargo
    
    @override
    def mostrar_info(self):
        print(f"{super().mostrar_info()}, Equipo a cargo: {self.__equipo_a_cargo} ")
        
    