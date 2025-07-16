class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome.strip().title()
        self.preco = float(preco)
        self.preco_inicial = float(preco)
        self.quantidade = int(quantidade)
    

    def total(self):
        return self.preco * self.quantidade

    def apresentar(self):
        return f'Nome: {self.nome:<20} | Qtd.: {self.quantidade:>4} | Valor Total: R${self.total():>10.2f}'
    
    def aplicar_desconto(self, porcentagem):
        self.preco *= (100 - porcentagem)/100


def separador():
    return f"{'-'*40}"


computador = Produto(nome= 'Computador', preco= 900, quantidade= 3)
me

produtos = (computador, mesa, aspirador)


for produto in produtos:
    print(f"""
{separador()}
{produto.apresentar()}""",end='')

    if produto == produtos[-1]:
        print(f'\n{separador()}')

print(f'Preço do computador antigo: {computador.preco}\nPreço Novo: {computador.aplicar_desconto(10)}')
print(f'{computador.preco}\n Novo -> {computador.aplicar_desconto(20)}')
print(computador.preco)