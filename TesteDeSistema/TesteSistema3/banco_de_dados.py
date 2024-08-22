class BancoDeDadosSimulado:
    def __init__(self):
        self.alunos = {}

    def adicionar_aluno(self, matricula, nome):
        self.alunos[matricula] = nome

    def buscar_aluno(self, matricula):
        return self.alunos.get(matricula)

    def remover_aluno(self, matricula):
        if matricula in self.alunos:
            del self.alunos[matricula]