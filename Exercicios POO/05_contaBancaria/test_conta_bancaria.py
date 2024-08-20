import unittest
from contaBancaria import Conta

class TesteContaBancaria(unittest.TestCase):

     def setUp(self):
         self.contabancaria1 = Conta("João")

     def test_depositar(self):
         self.assertEqual(self.contabancaria1.titular,"João")
         self.assertEqual(self.contabancaria1.saldo, 0)

         self.contabancaria1.depositar(500)
         self.assertEqual(self.contabancaria1.saldo, 500)

     def test_sacar(self):
         self.contabancaria1.depositar(500)
         self.contabancaria1.sacar(200)
         self.assertEqual(self.contabancaria1.saldo, 300)

     def test_sacar_mais_que_o_saldo(self):
         self.contabancaria1.depositar(500)
         with self.assertRaises(Exception):
             self.contabancaria1.sacar(1000)


if __name__ == '__main__':
    unittest.main()

