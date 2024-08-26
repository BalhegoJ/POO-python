import unittest
from calculadora import Calculadora
class TesteCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_add_dois_numeros(self):
        result = self.calculadora.add(20,60)
        self.assertEqual(20 + 60, result)

        result = self.calculadora.add(20.56, 60.89)
        self.assertEqual(20.56 + 60.89, result)

    def test_add_com_dois_numeros_invalidos_retorna_Type_Error(self):
        self.assertRaises(TypeError, self.calculadora.add, "Hello", "World")
        self.assertRaises(TypeError, self.calculadora.add, 20, "World")
        self.assertRaises(TypeError, self.calculadora.add, "Hello", 20)
        self.assertRaises(TypeError, self.calculadora.add, " 60.10.20.3", 20)

    def test_add_strings_numericas(self):
        result = self.calculadora.add("50", "60.7")
        self.assertEqual(50 + 60.7, result)

        result = self.calculadora.add(50, "60.7")
        self.assertEqual(50 + 60.7, result)

        result = self.calculadora.add("50", 60.7)
        self.assertEqual(50 + 60.7, result)


if __name__ == '__main__':
    unittest.main()
