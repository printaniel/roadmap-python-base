"""💪 Mini-proyecto (aplica todo lo anterior):
Crea un pequeño sistema de usuarios:

Clase base: Usuario con nombre y email.

Clase hija: Cliente, con atributo saldo encapsulado.

Clase hija: Administrador, que puede modificar el saldo de cualquier cliente.

Incluye polimorfismo: 
todos los usuarios deben tener un método mostrar_rol() que imprima distinto texto según su clase."""

from abc import ABC, abstractmethod
from typing import override

class Usuario(ABC):
    
    def __init__(self, nombre, email):
        self._nombre = nombre
        self._email = email
        
    @abstractmethod
    def mostrar_rol(self):
        pass

class Cliente(Usuario):
    
    def __init__(self, nombre, email, saldo):
        super().__init__(nombre, email)
        self.__saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0):
            raise ValueError("El saldo no puede ser negativo")
        self.__saldo = saldo
    
    @override
    def mostrar_rol(self):
        print("Cliente")
        
class Administrador(Usuario):
    
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        
    @override
    def mostrar_rol(self):
        print("Administrador")
    
    def modificar_saldo_cliente(self, cliente, saldo):
        if not isinstance(cliente, Cliente):
            raise TypeError("Solo se puede modificar el saldo de Clientes")
        cliente.saldo = saldo
        

    
    
    