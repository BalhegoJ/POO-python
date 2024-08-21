import unittest
from Banco_de_Dados_Simulado import BancoDeDadosSimulado
from servico_de_usuario import ServicoDeUsuario

class TesteServicoDeUsuario(unittest.TestCase):
    def setUp(self):
        self.banco_de_dados = BancoDeDadosSimulado()
        self.servico_de_usuario = ServicoDeUsuario(self.banco_de_dados)

    def test_criar_e_obter_usuario(self):
        self.servico_de_usuario.criar_usuario(1, 'João')
        usuario = self.servico_de_usuario.obter_usuario(1)

        self.assertEqual(usuario, 'João')

    def test_nao_permitir_criar_usuario_com_mesmo_id(self):
        self.servico_de_usuario.criar_usuario(1, 'João')

        with self.assertRaises(ValueError):
            self.servico_de_usuario.criar_usuario(1, 'Maria')

    def test_deletar_usuario(self):
        self.servico_de_usuario.criar_usuario(1, 'João')
        self.servico_de_usuario.deletar_usuario(1)

        with self.assertRaises(ValueError):
            self.servico_de_usuario.obter_usuario(1)

    def test_obter_usario_inexistente(self):
        with self.assertRaises(ValueError):
            self.servico_de_usuario.obter_usuario(1)

if __name__ == '__main__':
    unittest.main()

