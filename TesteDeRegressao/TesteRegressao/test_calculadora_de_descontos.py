import unittest
from Calculadora_de_desconto import CalculadoraDeDescontos


class TesteDeRegressaoCalculadoraDeDescontos(unittest.TestCase):
    def setUp(self):
        self.calculadora = CalculadoraDeDescontos()

    def test_aplicar_desconto_fixo(self):
        # Testar desconto fixo com valor válido
        resultado = self.calculadora.aplicar_desconto_fixo(100, 20)
        self.assertEqual(resultado, 80)

        # Testar desconto fixo com desconto maior que o valor
        resultado = self.calculadora.aplicar_desconto_fixo(50, 60)
        self.assertEqual(resultado, 0)

        # Testar desconto fixo com valor zero
        resultado = self.calculadora.aplicar_desconto_fixo(0, 20)
        self.assertEqual(resultado, 0)

    def test_aplicar_desconto_percentual(self):
        # Testar desconto percentual válido
        resultado = self.calculadora.aplicar_desconto_percentual(100, 10)
        self.assertEqual(resultado, 90)

        # Testar desconto percentual de 100%
        resultado = self.calculadora.aplicar_desconto_percentual(100, 100)
        self.assertEqual(resultado, 0)

        # Testar desconto percentual de 0%
        resultado = self.calculadora.aplicar_desconto_percentual(100, 0)
        self.assertEqual(resultado, 100)

    def test_aplicar_desconto_progressivo(self):
        # Testar desconto progressivo para valor abaixo de 500 (sem desconto)
        resultado = self.calculadora.aplicar_desconto_progressivo(400)
        self.assertEqual(resultado, 400)

        # Testar desconto progressivo para valor entre 500 e 1000 (5% de desconto)
        resultado = self.calculadora.aplicar_desconto_progressivo(800)
        self.assertEqual(resultado, 760)

        # Testar desconto progressivo para valor acima de 1000 (10% de desconto)
        resultado = self.calculadora.aplicar_desconto_progressivo(1500)
        self.assertEqual(resultado, 1350)

    def test_regressao_desconto_fixo(self):
        # Garantir que a funcionalidade de desconto fixo não foi quebrada após adição de novas funcionalidades
        resultado = self.calculadora.aplicar_desconto_fixo(200, 50)
        self.assertEqual(resultado, 150)

    def test_regressao_desconto_percentual(self):
        # Garantir que a funcionalidade de desconto percentual não foi quebrada após adição de novas funcionalidades
        resultado = self.calculadora.aplicar_desconto_percentual(200, 25)
        self.assertEqual(resultado, 150)


if __name__ == '__main__':
    unittest.main()