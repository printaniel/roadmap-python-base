""" Qué practicar:

Diferencia entre atributos de instancia y métodos

Usar self correctamente

💪 Ejercicios:

Crea una clase CuentaBancaria con atributos: titular, saldo.

Agrega métodos depositar() y retirar(). Que actualicen el saldo.

Agrega un método mostrar_saldo() que imprima el saldo actual.

Crea 2 cuentas distintas y haz operaciones sobre ellas."""

class CuentaBancaria:
    
    def __init__(self, titular,saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, saldoEntrante):
        self.saldo += saldoEntrante
        
    def retirar(self, saldoRetirar):
        self.saldo -= saldoRetirar
        
    def mostrarSaldo(self):
        print(f"Saldo Actual: {self.saldo}")
        
        
        
cuenta_1 = CuentaBancaria("Aniel Varela", 3000)
cuenta_2 = CuentaBancaria("Raul Hechaverria", 1600)

cuenta_1.depositar(5000)
cuenta_1.retirar(2000)
cuenta_2.depositar(500)
cuenta_2.retirar(600)
cuenta_1.mostrarSaldo()
cuenta_2.mostrarSaldo()