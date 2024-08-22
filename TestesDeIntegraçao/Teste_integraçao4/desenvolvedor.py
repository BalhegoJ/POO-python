from funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome, sobrenome, salario, linguagemProgramaçao, senioridade):
        super().__init__(nome, sobrenome, salario)
        self.linguagemProgramaçao = linguagemProgramaçao
        self.senioridade = senioridade