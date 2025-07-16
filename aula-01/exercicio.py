class Pessoa:

    def __init__(self, altura, idade):

        self.altura = float(altura)
        self.idade = int(idade)

    def correr(self):
        return f'A pessoa está correndo...'

    def comer(self):
        return f'A pessoa está comendo'
    
    def apresentacao(self, nome):
        return f'Olá, sou {nome}, Tenho {self.altura} cm e {self.idade} anos'
    
joao = Pessoa(altura= 170, idade= 20)