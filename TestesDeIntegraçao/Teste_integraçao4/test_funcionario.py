import unittest
from funcionario import Funcionario

class TesteFuncionario(unittest.TestCase):
    def setUp(self):
        self.funcionario1 = Funcionario('Anderson', 'Lima', 3000)

    def test_aumentar_salario(self):
        self.assertEqual(self.funcionario1.nome, 'Anderson')
        self.assertEqual(self.funcionario1.sobrenome, 'Lima')
        self.assertEqual(self.funcionario1.salario, 3000)
        self.assertEqual(self.funcionario1.email, 'Anderson.Lima@gmail.com')

        self.funcionario1.aumentar_salario()
        self.assertEqual(self.funcionario1.salario, 3150)

    if __name__ == '__main__':
        unittest.main()



