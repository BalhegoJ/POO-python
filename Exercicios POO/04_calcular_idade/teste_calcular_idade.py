import unittest
from calcular_idade import Pessoa
from datetime import date

class TestePessoa(unittest.TestCase):
    def setUp(self):
        self.pessoa1 = Pessoa('João Victor', 'Brasil', date(2001, 4, 19))
        self.pessoa2 = Pessoa('Gustavo Odolin', 'Brasil', date.today())
        self.pessoa3 = Pessoa('Kauan Dalfovo', 'Brasil', date(2006, 12, 11))
        self.pessoa4 = Pessoa('Giulia', 'Brasil', date(2024, 12, 31))

    def test_calcular_idade(self):
        self.assertEqual(self.pessoa1.nome, 'João Victor')
        self.assertEqual(self.pessoa1.pais_de_nascimento, 'Brasil')
        self.assertEqual(self.pessoa1.data_de_nascimento, date(2001, 4, 19))

        self.assertEqual(self.pessoa1.calcular_idade(), 23)

    def test_calcular_idade_negativa(self):
        self.assertEqual(self.pessoa4.calcular_idade(), -1)

    def teste_calcular_idade_zerada(self):
        self.assertEqual(self.pessoa2.calcular_idade(), 0)

if __name__ == '__main__':
    unittest.main()



