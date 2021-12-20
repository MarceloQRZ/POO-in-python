class Poduto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual / 100)

    # getters
    @property
    def preco(self):
        return self._preco

    # setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


p1 = Poduto('camisa', 50)
p1.desconto(10)
print(p1.preco)

p2 = Poduto('camisa', 'R$100')
p2.desconto(10)
print(p2.preco)
