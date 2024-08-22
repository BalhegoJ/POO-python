import unittest
from desenvolvedor import Desenvolvedor

class TesteDesenvolvedor(unittest.TestCase):
    def setUp(self):
        self.dev1 = Desenvolvedor('João', 'Balhego', 5000, 'Python', 'Pleno')

    def test_aumentar_salario(self):
        self.assertEqual(self.dev1.nome, 'João')
        self.assertEqual(self.dev1.sobrenome, 'Balhego')
        self.assertEqual(self.dev1.email, 'João.Balhego@gmail.com')
        self.assertEqual(self.dev1.salario, 5000)
        self.assertEqual(self.dev1.linguagemProgramaçao, 'Python')
        self.assertEqual(self.dev1.senioridade, 'Pleno')

        self.dev1.aumentar_salario()
        self.assertEqual(self.dev1.salario, 5250)

if __name__ == '__main__':
    unittest.main()