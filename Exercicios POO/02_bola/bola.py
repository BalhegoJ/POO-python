class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novaCor):
        print ("-----Nova cor-----")
        self.cor = novaCor


bola1 = Bola("Vermelha", "20 cm", "Borracha")
print('cor: ', bola1.cor)
print('circunferencia: ', bola1.circunferencia)
print('material: ', bola1.material)

bola1.trocaCor('Azul')
print('cor: ', bola1.cor)
