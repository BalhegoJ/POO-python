import unittest
from Gerenciador_de_estoque import GerenciadorDeEstoque

class TesteGerenciadorDeEstoque(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorDeEstoque()

    def test_criar_e_listar_estoque(self):
        self.gerenciador.cadastrar_item(1, 'Cimento')
        self.gerenciador.cadastrar_item(2, 'Tijolo')
        self.gerenciador.cadastrar_item(3, 'Bitoneira')

        estoque = self.gerenciador.listar_itens()
        self.assertEqual(len(estoque), 3)
        self.assertEqual(estoque[1], 'Cimento')
        self.assertEqual(estoque[2], 'Tijolo')
        self.assertEqual(estoque[3], 'Bitoneira')

    def test_editar_item(self):
        self.gerenciador.cadastrar_item(1, 'Cimento')
        self.gerenciador.editar_item(1, 'Tijolo')

        item = self.gerenciador.listar_itens()[1]
        self.assertEqual(item, 'Tijolo')

    def test_excluir_item(self):
        self.gerenciador.cadastrar_item(1, 'Cimento')
        self.gerenciador.excluir_item(1)

        estoque = self.gerenciador.listar_itens()
        self.assertNotIn(1, estoque)

    def test_fluxo_completo_de_uso(self):
        # Criação e Verificação de itens
        self.gerenciador.cadastrar_item(1, 'Cimento')
        self.gerenciador.cadastrar_item(2, 'Tijolo')
        self.gerenciador.cadastrar_item(3, 'Bitoneira')

        estoque = self.gerenciador.listar_itens()
        self.assertEqual(len(estoque), 3)
        self.assertEqual(estoque[1], 'Cimento')
        self.assertEqual(estoque[2], 'Tijolo')
        self.assertEqual(estoque[3], 'Bitoneira')

        # Edição de Itens
        self.gerenciador.editar_item(1, 'Tijolo')

        item = self.gerenciador.listar_itens()[1]
        self.assertEqual(item, 'Tijolo')

        # Exclusão de Itens
        self.gerenciador.excluir_item(1)

        estoque = self.gerenciador.listar_itens()
        self.assertNotIn(1, estoque)

if __name__ == '__main__':
    unittest.main()