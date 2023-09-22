#crie uma classe chamada produto com atributos nome e preço e quantidade.
#implemente um metodo chamado calcular_total que retorne o valor total do produto
class produto:
    def calcular_total(self, nome, preço, quantidade):
        total = preço * quantidade
        print(f'comprou {nome} pelo preço de R${preco} e {quantidade} unidades, o total ficou por R${total}')