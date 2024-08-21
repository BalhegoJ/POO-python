class BancoDeDadosSimulado:
    def __init__(self):
        self.funcionarios = {}

    def adicionar_funcionario(self, id_funcionario, nome):
        self.funcionarios[id_funcionario] = nome

    def buscar_funcionario(self, id_funcionario):
        return self.funcionarios.get(id_funcionario)

    def deletar_funcionario(self, id_funcionario):
        if id_funcionario in self.funcionarios:
            del self.funcionarios[id_funcionario]

