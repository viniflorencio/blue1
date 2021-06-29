#2) Crie uma classe chamada Conta para simular as operações de
#uma conta corrente. Sua classe deverá ter os atributos Titular e
#Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
#Conta e teste os atributos e métodos implementados.




class Conta:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self,saque):
        
        self.saldo -= saque

    def depositar(self,deposito):
        self.saldo += deposito



cliente = Conta('Vinicius', 2300)
print(cliente.titular)
print(cliente.saldo)
print()
cliente.depositar(100)
print(cliente.saldo)

