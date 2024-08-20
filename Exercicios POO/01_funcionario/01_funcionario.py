class Funcionario:
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        self.email = nome + '.' + sobrenome + '@gmail.com'

    def salario_aumento(self):
        print('-------aumento de salario-------')
        self.salario = self.salario * 1.05


    def mostrar(self):
        print('nome: ', self.nome)
        print('sobrenome: ', self.sobrenome)
        print('Salario: ', self.salario)
        print('Email: ', self.email)

pessoa1 = Funcionario('Ricardo\n', 'pasqualine\n', 2500)
pessoa2 = Funcionario('João Victor\n', 'Balhego\n', 6800)
pessoa3 = Funcionario('Antonio\n', 'Marcos\n', 9000)
pessoa4 = Funcionario('Patrick\n', 'Severo\n', 6500)


print('nome: ', pessoa1.nome,'sobrenome: ',pessoa1.sobrenome,'salario: R$',pessoa1.salario,'\nemail: ',pessoa1.email)
pessoa1.salario_aumento()
print(pessoa1.salario)
print('\n')
print('nome: ', pessoa2.nome, 'sobrenome: ',pessoa2.sobrenome, 'salario: R$',pessoa2.salario, '\nemail: ',pessoa2.email)
pessoa2.salario_aumento()
print(pessoa2.salario)
print('\n')
print('nome: ', pessoa3.nome, 'sobrenome: ',pessoa3.sobrenome, 'salario: R$',pessoa3.salario, '\nemail: ',pessoa3.email)
pessoa3.salario_aumento()
print(pessoa3.salario)
print('\n')
print('nome: ', pessoa4.nome, 'sobrenome: ',pessoa4.sobrenome, 'salario: R$',pessoa4.salario, '\nemail: ',pessoa4.email)
pessoa4.salario_aumento()
print(pessoa4.salario)
