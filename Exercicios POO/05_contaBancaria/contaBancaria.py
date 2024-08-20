class Conta:

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
         self.saldo -= valor
        else:
            raise Exception('O valor de saque é maior que o saldo')

#conta = Conta("João")
#conta.depositar(1000)
#conta.sacar(500)
#conta.sacar(700)
#print("Saldo final: R$ {:.2f}".format(conta.saldo))
