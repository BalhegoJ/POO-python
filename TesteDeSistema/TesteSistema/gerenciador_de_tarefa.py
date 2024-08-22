class GerenciadorDeTarefa:
    def __init__(self, descricao):
        self.descricao = descricao


class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = {}

    def criar_tarefa(self, id_tarefa, descricao):
        if id_tarefa in self.tarefas:
            raise ValueError("Tarefa com esse ID já existe.")
        self.tarefas[id_tarefa] = Tarefa(descricao)

    def listar_tarefas(self):
        return {id_tarefa: tarefa.descricao for id_tarefa, tarefa in self.tarefas.items()}

    def editar_tarefa(self, id_tarefa, nova_descricao):
        if id_tarefa not in self.tarefas:
            raise ValueError("Tarefa não encontrada.")
        self.tarefas[id_tarefa].descricao = nova_descricao

    def excluir_tarefa(self, id_tarefa):
        if id_tarefa not in self.tarefas:
            raise ValueError("Tarefa não encontrada.")
        del self.tarefas[id_tarefa]


