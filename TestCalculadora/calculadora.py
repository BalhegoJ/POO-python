class Calculadora:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):

        return self.x + self.y

    def sub(self):

        return self.x - self.y

    def mult(self):

        return self.x * self.y

    def div(self):
        if (self.y == 0):
            print('O denominador não pode ser igual a zero')
            return None
        else:

            return self.x / self.y


soma = Calculadora(10, 12)
subtraçao = Calculadora(25, 13)
multiplica = Calculadora(32, 17)
divisao = Calculadora(120, 6)

print(soma.add())
print(subtraçao.sub())
print(multiplica.mult())
print(divisao.div())
