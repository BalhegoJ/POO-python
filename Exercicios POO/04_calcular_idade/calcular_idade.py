from datetime import date

class Pessoa:
    def __init__(self, nome, pais_de_nascimento, data_de_nascimento):
        self.nome = nome
        self.pais_de_nascimento = pais_de_nascimento
        self.data_de_nascimento = data_de_nascimento

    def calcular_idade(self):
        hoje = date.today()
        idade = hoje.year - self.data_de_nascimento.year

        if hoje < date(hoje.year, self.data_de_nascimento.month, self.data_de_nascimento.day):
            idade -= 1

        return idade

pessoa1 = Pessoa("Guilherme", "Brasil", date(1994, 8, 11))
print("Idade: ", pessoa1.calcular_idade())
