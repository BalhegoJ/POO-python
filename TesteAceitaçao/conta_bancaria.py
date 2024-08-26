class ContaBancaria:
    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, quantia):
        if quantia <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += quantia

    def sacar(self, quantia):
        if quantia > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= quantia

    def verificar_saldo(self):
        return self.saldo