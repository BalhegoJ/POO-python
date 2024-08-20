import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_add(self):
        calculadora = Calculadora(20,10)
        self.assertEqual(calculadora.add(), 30)

    def test_sub(self):
        calculadora = Calculadora(20,10)
        self.assertEqual(calculadora.sub(), 10)

    def test_mult(self):
        calculadora = Calculadora(20,10)
        self.assertEqual(calculadora.mult(), 200)

    def test_div(self):
        calculadora = Calculadora(20,10)
        self.assertEqual(calculadora.div(), 2)


if __name__ == '__main__':
    unittest.main()


