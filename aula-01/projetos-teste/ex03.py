# No método sacar, adicione uma verificação para não sacar mais que o saldo.
# Se o valor for maior que o saldo, imprima "Saldo insuficiente".


class Conta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo_inicial = saldo
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):

        if valor > self.saldo:
            print('Saldo Insuficiente!')
        else:
            self.saldo -= valor
    
    def apresentar(self):
        return f'Titular: {self.titular} - Saldo: R$ {self.saldo:.2f}'

def separador():
    return '-=' * 20


juliano = Conta('Juliano', 1000)
marcos = Conta('Marcos', 250.24)
sofia = Conta('Sofia', 780.23)

print(separador())

print(juliano.apresentar())
print(marcos.apresentar())
print(sofia.apresentar())

print(separador(), 'Juliano Depositou 250', separador())

juliano.depositar(250)
marcos.depositar(100.01)
sofia.sacar(80.23)


print(juliano.apresentar())
print(marcos.apresentar())
print(sofia.apresentar())

print(separador())

juliano.sacar(1000)
marcos.sacar(150.25)
sofia.depositar(300)

print(juliano.apresentar())
print(marcos.apresentar())
print(sofia.apresentar())

