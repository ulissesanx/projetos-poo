# Crie uma classe chamada Pessoa com os atributos nome e idade.
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome.strip().title()
        self.idade = int(idade)

    def apresentar(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}'



# Crie dois objetos Pessoa diferentes e imprima os dados deles.

pessoa_marcos = Pessoa('Marcos', 17)

pessoa_joao = Pessoa('Joao', 13)

print('========DADOS=========')
print(f'{pessoa_joao.apresentar()}\n======================\n{pessoa_marcos.apresentar()}')
print('======================')