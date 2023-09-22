#crie uma classe chamada contabancaria que tenha atributos saldo e titular.
# implemente um metodo de depositar e sacar para manipular o saldo.
class ContaBancaria():

    def __init__(self, titular): 
        self.titular = titular
        self.saldo = 0

    def depositou(self, depositar):
        self.depositar = depositar
        resultado = self.saldo + depositar
        print(self.titular, 'DEPOSITOU ', depositar)
        print('Você tem o saldo de R$', self.saldo)
    

    def sacou(self, sacar):
        self.sacar = sacar
        resultado = self.saldo - sacar
        print(self.titular, 'SACOU', sacar)
        print('Você tem o saldo de R$', self.saldo)

conta1 = ContaBancaria('uictor')

print(conta1.sacou(100))
print(conta1.depositou(1000))
