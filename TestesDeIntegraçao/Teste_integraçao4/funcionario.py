class Funcionario:
    taxa_incrementar_salario = 1.05

    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.email = nome + "." + sobrenome + "@gmail.com"

    def aumentar_salario(self):
        self.salario = int(self.salario * self.taxa_incrementar_salario)