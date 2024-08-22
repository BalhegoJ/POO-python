class ServicoDeAluno:
    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def matricular_aluno(self, matricula, nome):
        if self.banco_de_dados.buscar_aluno(matricula):
            raise ValueError("Aluno já está matriculado")
        self.banco_de_dados.adicionar_aluno(matricula, nome)

    def obter_aluno(self, matricula):
        aluno = self.banco_de_dados.buscar_aluno(matricula)
        if not aluno:
            raise ValueError("Aluno não cadastrado no sistema")
        return aluno

    def deletar_aluno(self, matricula):
        if not self.banco_de_dados.buscar_aluno(matricula):
            raise ValueError("Aluno não cadastrado no sistema")
        self.banco_de_dados.remover_aluno(matricula)