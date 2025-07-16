class CadastrarPessoa:

    def __init__(self, idade: int, nome: str):
        self.atributo_idade = idade
        self.atributo_nome = nome

    def metodo_dois(self):
        return self.atributo_idade
    



pessoa = CadastrarPessoa(idade= 15, nome= 'Jefferson')

print(pessoa.metodo_dois())