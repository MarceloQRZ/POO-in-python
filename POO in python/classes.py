class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} nao pode falar comendo!')
            return
        elif self.falando:
            print(f'{self.nome} ja esta falando!')
            return

        print(f'{self.nome} esta falando {assunto} ')
        self.falando = True

    def pararFalar(self):
        if self.falando == False:
            print(f'{self.nome} nao esta falando!')
        else:
            self.falando = False
            print(f'{self.nome} parou de falar!')

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} nao pode comer enquanto fala.')
            return
        if self.comendo:
            print(f'{self.nome} ja esta comendo!')
            return

        print(f'{self.nome} esta comendo {alimento} ')
        self.comendo = True

    def pararComer(self):
        if self.comendo == False:
            print(f'{self.nome} nao esta comendo!')
        else:
            self.comendo = False
            print(f'{self.nome} parou de comer!')


p1 = Pessoa('Zé', 33)
p1.comer('frutas')
p1.falar('besteira')
p1.pararComer()
p1.falar('besteira')
p1.comer('frutas')