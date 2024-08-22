import unittest
from gerenciador_de_tarefa import GerenciadorDeTarefas


class TesteDeSistemaGerenciadorDeTarefas(unittest.TestCase):
    def setUp(self):
        self.gerenciador = GerenciadorDeTarefas()

    def test_criar_e_listar_tarefas(self):
        # Criar algumas tarefas
        self.gerenciador.criar_tarefa(1, "Comprar leite")
        self.gerenciador.criar_tarefa(2, "Estudar para a prova")

        # Verificar se as tarefas foram criadas corretamente
        tarefas = self.gerenciador.listar_tarefas()
        self.assertEqual(len(tarefas), 2)
        self.assertEqual(tarefas[1], "Comprar leite")
        self.assertEqual(tarefas[2], "Estudar para a prova")

    def test_editar_tarefa(self):
        # Criar uma tarefa
        self.gerenciador.criar_tarefa(1, "Comprar leite")

        # Editar a tarefa
        self.gerenciador.editar_tarefa(1, "Comprar pão")

        # Verificar se a tarefa foi editada corretamente
        tarefa = self.gerenciador.listar_tarefas()[1]
        self.assertEqual(tarefa, "Comprar pão")

    def test_excluir_tarefa(self):
        # Criar uma tarefa
        self.gerenciador.criar_tarefa(1, "Comprar leite")

        # Excluir a tarefa
        self.gerenciador.excluir_tarefa(1)

        # Verificar se a tarefa foi excluída
        tarefas = self.gerenciador.listar_tarefas()
        self.assertNotIn(1, tarefas)

    def test_fluxo_completo_de_uso(self):
        # Criar e verificar a criação das tarefas
        self.gerenciador.criar_tarefa(1, "Comprar leite")
        self.gerenciador.criar_tarefa(2, "Estudar para a prova")
        tarefas = self.gerenciador.listar_tarefas()
        self.assertEqual(len(tarefas), 2)

        # Editar e verificar a edição de uma tarefa
        self.gerenciador.editar_tarefa(1, "Comprar pão")
        tarefa = self.gerenciador.listar_tarefas()[1]
        self.assertEqual(tarefa, "Comprar pão")

        # Excluir e verificar a exclusão de uma tarefa
        self.gerenciador.excluir_tarefa(2)
        tarefas = self.gerenciador.listar_tarefas()
        self.assertEqual(len(tarefas), 1)
        self.assertNotIn(2, tarefas)


if __name__ == '__main__':
    unittest.main()