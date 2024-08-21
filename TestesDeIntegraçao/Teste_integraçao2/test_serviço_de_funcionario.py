import unittest
from banco_de_dados import BancoDeDadosSimulado
from servico_de_funcionario import ServicoDeFuncionario

class TesteServiçoDeFuncionario(unittest.TestCase):
    def setUp(self):
        self.banco_de_dados = BancoDeDadosSimulado()
        self.servico_de_funcionario = ServicoDeFuncionario(self.banco_de_dados)

    def test_criar_e_obter_usuario(self):
        self.servico_de_funcionario.criar_funcionario(1, 'Giulia')
        funcionario = self.servico_de_funcionario.obter_funcionario(1)

        self.assertEqual (funcionario, 'Giulia')

    def test_nao_permitir_criar_usuario_com_mesmo_id(self):
        self.servico_de_funcionario.criar_funcionario(1, 'Giulia')

        with self.assertRaises(ValueError):
            self.servico_de_funcionario.criar_funcionario(1, 'Kauan')

    def deletar_usuario(self):
        self.servico_de_funcionario.criar_funcionario(1, 'Giulia')
        self.servico_de_funcionario.deletar_funcionario(1)

        with self.assertRaises(ValueError):
            self.servico_de_funcionario.obter_funcionario(1)

    def test_obter_funionario_inexistente(self):
        with self.assertRaises(ValueError):
            self.servico_de_funcionario.obter_funcionario(1)

if __name__ == 'main':
    unittest.main()
