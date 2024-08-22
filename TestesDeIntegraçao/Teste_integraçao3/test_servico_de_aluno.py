import unittest
from banco_de_dados import BancoDeDados
from servico_de_aluno import ServicoDeAluno

class TesteServicoDeAluno(unittest.TestCase):
    def setUp(self):
        self.banco_de_dados = BancoDeDados()
        self.servico_de_aluno = ServicoDeAluno(self.banco_de_dados)

    def test_criar_e_buscar_aluno(self):
        self.servico_de_aluno.matricular_aluno(123456, "Guilherme")
        self.assertEqual(self.servico_de_aluno.obter_aluno(123456), "Guilherme")

    def test_criar_aluno_com_mesma_id(self):
        self.servico_de_aluno.matricular_aluno(123456, "Guilherme")
        with self.assertRaises(ValueError):
            self.servico_de_aluno.matricular_aluno(123456, "João")

    def test_deletar_aluno(self):
        self.servico_de_aluno.matricular_aluno(123456, "Guilherme")
        self.servico_de_aluno.deletar_aluno(123456)
        with self.assertRaises(ValueError):
            self.servico_de_aluno.obter_aluno(123456)

    def test_buscar_aluno_inexistente_no_banco_de_dados(self):
        with self.assertRaises(ValueError):
            self.servico_de_aluno.obter_aluno(123456)

if __name__ == '__main__':
    unittest.main()