class Calculadora:
    def add(self, x, y):
        if not isinstance(x, int) and not isinstance(x, float):
            if not x.replace('.', '', 1).isnumeric():
                raise TypeError
            x = float(x)
        if not isinstance(y, int) and not isinstance(y, float):
            if not y.replace('.', '', 1).isnumeric():
              raise TypeError
            y = float(y)
        return x + y
    def subt(self, x, y):
        pass

    def multiplicaçao(self, x, y):
        pass

    def divisao(self, x, y):
        pass
