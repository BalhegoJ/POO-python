class CalculadoraDeDescontos:
    def __init__(self):
        pass

    def aplicar_desconto_fixo(self, valor, desconto):
        if desconto < 0:
            raise ValueError("O desconto deve ser positivo.")
        return max(0, valor - desconto)

    def aplicar_desconto_percentual(self, valor, percentual):
        if percentual < 0 or percentual > 100:
            raise ValueError("O percentual de desconto deve estar entre 0 e 100.")
        return valor * ((100 - percentual) / 100)

    def aplicar_desconto_progressivo(self, valor):
        if valor > 1000:
            return valor * 0.9  # 10% de desconto para compras acima de 1000
        elif valor > 500:
            return valor * 0.95  # 5% de desconto para compras entre 500 e 1000
        else:
            return valor  # Sem desconto para compras abaixo de 500