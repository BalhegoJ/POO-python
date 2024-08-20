import unittest
from retangulo import Retangulo

class TesteRetangulo(unittest.TestCase):
    def setUp(self):
        self.Retangulo = Retangulo(5,3)

    def teste_calculo_area(self):
        self.assertEqual(self.Retangulo.largura, 5)
        self.assertEqual(self.Retangulo.altura, 3)

        area = self.Retangulo.calcurar_area()
        self.assertEqual(area, 15)

if __name__ == '__main__':
    unittest.main()





