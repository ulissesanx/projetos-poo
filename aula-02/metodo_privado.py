class RegistrarPessoa:

    def __init__(self, nome, cpf, rg, idade):
        
        self.nome = str(nome)
        self.__cpf = str(cpf)
        self.__rg = str(rg)
        self.idade = int(idade)
        self.ano_de_nascimento = self.ano_nascimento()

    def ano_nascimento(self):
        from datetime import date
        ano_atual = date.today().year

        return ano_atual - self.idade
    
    def __passar_dados(self):
        return f"""
RG: {self.__rg}
CPF: {self.__cpf}"""
    
    def ficha(self):
        return f"""
Nome: {self.nome}
Idade: {self.idade}
Ano de Nascimento: {self.ano_de_nascimento}
{self.__passar_dados()}
"""
    
joao = RegistrarPessoa(nome= 'João', cpf= '549.125.928045', rg= '655892530', idade= 21)

