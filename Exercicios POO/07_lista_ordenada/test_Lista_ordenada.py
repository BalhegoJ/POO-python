import unittest
import ListaOrdenada

class TestListaOrdenada(unittest.TestCase):
    def test_lista_ordenada(self):
        lista = [1, 2, 3, 4, 5, 6, 7]

        self.assertTrue(ListaOrdenada.lista_ordenada(lista))

    def test_lista_nao_ordenada(self):
        lista = [1, 6, 4, 12, 8, 7]
        self.assertFalse(ListaOrdenada.lista_ordenada(lista))

    if __name__ == '__main__':
        unittest.main()
