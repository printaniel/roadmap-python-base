"""✅ Qué practicar:

Atributos privados (_protegido, __privado)

Métodos getter y setter

Decoradores @property y @<atributo>.setter

💪 Ejercicios (sin respuestas):

Crea una clase CuentaBancaria con atributo privado __saldo. 
Implementa métodos para obtener y modificar el saldo usando @property.

Evitá que el saldo pueda ser menor que cero usando validación en el setter.

Agregá un método público mostrar_info() que imprima el saldo,
y un método privado __registro_interno() que no deba ser accesible desde fuera"""

class CuentaBancaria:
    
    def __init__(self, saldo):
        self.__saldo = saldo
        self.__transacciones = 0
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,saldo):
        if(saldo<0):
            raise ValueError("El saldo no puede ser negativo")
        
        self.__saldo = saldo
        self.__registro_interno()
        
            
    def mostrar_info(self):
        print(f"Saldo Actual: {self.saldo}")
    
    def  __registro_interno(self):
        self.__transacciones +=1
        print(f"[Registro interno] Transacciones totales: {self.__transacciones}")
        
        
cuenta = CuentaBancaria(100)
cuenta.mostrar_info()    # Saldo Actual: 100
cuenta.saldo = 200       # [Registro interno] Transacciones totales: 2
  
        