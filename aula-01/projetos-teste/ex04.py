# Crie uma classe Aluno com atributos nome e uma lista de notas.
# Adicione um método adicionar_nota(nota) e outro calcular_media().

class Aluno:

    def __init__(self, nome, lista_notas=[]):
        self.nome = nome
        self.lista_notas = lista_notas

    def adicionar_nota(self, nota):
        self.lista_notas.append(nota)

    def calcular_media(self):
        tamanho_lista = len(self.lista_notas)
        return sum(self.lista_notas)/tamanho_lista if tamanho_lista else '- Nao há nenhuma nota adicionada'

    def mostrar_media(self):
        return f'As notas de {self.nome} são {self.lista_notas} e a média delas é {self.calcular_media()}'

joao = Aluno('Joao')

# Crie um aluno, adicione 3 notas e mostre a média.
