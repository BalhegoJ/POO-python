import unittest
from bola import Bola

class TesteBola(unittest.TestCase):
    def setUp(self):
        self.bola1 = Bola("Vermelha", "20cm", "Borracha")

    def test_criaçao_objeto(self):
        self.assertEqual(self.bola1.cor, "Vermelha")
        self.assertEqual(self.bola1.circunferencia, "20cm")
        self.assertEqual(self.bola1.material, "Borracha")


    def test_troca_cor(self):
        self.bola1.trocaCor("Azul")
        self.assertEqual(self.bola1.cor, "Azul")

    if __name__ == '__main__':
        unittest.main()