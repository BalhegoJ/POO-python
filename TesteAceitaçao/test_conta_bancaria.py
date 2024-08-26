import unittest
from conta_bancaria import ContaBancaria


class TesteDeAceitacaoContaBancaria(unittest.TestCase):
    def test_fluxo_completo_de_uso(self):
        # Requisito 1 - criar uma conta bancaria com saldo inicial
        Conta = ContaBancaria('João', 100)
        # Verificar o saldo incial
        self.assertEqual(Conta.verificar_saldo(), 100)

        # Requisito 2 - Depositar dinheiro na conta
        Conta.depositar(50)
        # Verificar saldo após o depósito
        self.assertEqual(Conta.verificar_saldo(), 150)

        # Requisito 3 - Sacar dinheiro na conta
        Conta.sacar(30)
        # Verificar o saldo após o saque
        self.assertEqual(Conta.verificar_saldo(), 120)

        # Requisito 4 - Tentar sacar mais que o saldo disponivél
        with  self.assertRaises(ValueError):
            Conta.sacar(200)

        # Verifica se o saldo permaneceu o mesmo após a tentativa inválida de saque
        self.assertEqual(Conta.verificar_saldo(), 120)


if __name__ == 'main_':
    unittest.main()