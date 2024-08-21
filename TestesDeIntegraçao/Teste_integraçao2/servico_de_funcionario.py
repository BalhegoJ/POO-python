class ServicoDeFuncionario:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def criar_funcionario(self, id_funcionario, nome):
        if self.banco_de_dados.buscar_funcionario(id_funcionario):
            raise ValueError("funcionario já existe")
        self.banco_de_dados.adicionar_funcionario(id_funcionario, nome)

    def obter_funcionario(self, id_funcionario):
        funcionario = self.banco_de_dados.buscar_funcionario(id_funcionario)
        if not funcionario:
            raise ValueError("funcionario não encontrado")
        return funcionario

    def deletar_funcionario(self, id_funconario):
        if not self.banco_de_dados.buscar_funcionario(id_funconario):
            raise ValueError("funcionario não encontrado")
        self.banco_de_dados.remover_funcionario(id_funconario)
        