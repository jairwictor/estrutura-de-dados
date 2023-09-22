#crie uma classe chamada carro com atributos marca, modelo e ano.
#implemente um metodo chamado detalhes que ret9orna uma string com as informações do carro.
 class carro:
     def detalhes(self, marca, modelo, ano):
         print(f'o modelo do carro é {modelo} da marca {marca} e ano de {ano}')

carro1 = carro()
carro1.detalhes('jipe', 'jeep', 2015)