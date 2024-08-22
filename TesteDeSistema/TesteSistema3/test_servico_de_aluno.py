import unittest
from servico_de_aluno import ServicoDeAluno
from banco_de_dados import BancoDeDadosSimulado

class TesteServicoDeAluno(unittest.TestCase):
    def setUp(self):
        self.banco_de_dados = BancoDeDadosSimulado()
        self.servico_de_aluno = ServicoDeAluno(self.banco_de_dados)

    def test_criar_e_buscar_aluno(self):
        self.servico_de_aluno.matricular_aluno(123456, 'João')
        aluno = self.servico_de_aluno.obter_aluno(123456)
        self.assertEqual(aluno, 'João')

    def test_nao_permitir_criar_aluno_com_mesma_matricula(self):
        self.servico_de_aluno.matricular_aluno(123456, 'João')
        with self.assertRaises(ValueError):
             self.servico_de_aluno.matricular_aluno(123456, 'Giulia')

    def test_deletar_aluno(self):
        self.servico_de_aluno.matricular_aluno(123456, 'João')
        self.servico_de_aluno.deletar_aluno(123456)
        with self.assertRaises(ValueError):
            self.servico_de_aluno.obter_aluno(123456)

    def test_obter_aluno_inexistente(self):
        with self.assertRaises(ValueError):
            self.servico_de_aluno.obter_aluno(123456)

    def test_fluxo_completo_do_sistema(self):
        self.servico_de_aluno.matricular_aluno(123456, 'João')
        aluno = self.servico_de_aluno.obter_aluno(123456)
        self.assertEqual(aluno, 'João')

        with self.assertRaises(ValueError):
            self.servico_de_aluno.matricular_aluno(123456, 'João')

        self.servico_de_aluno.deletar_aluno(123456)
        with self.assertRaises(ValueError):
            self.servico_de_aluno.obter_aluno(123456)

        with self.assertRaises(ValueError):
            self.servico_de_aluno.obter_aluno(123456)


if __name__ == '__main__':
    unittest.main()


