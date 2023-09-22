#crie uma classe chamada pessoa com atributos nome e idade. 
#implemente um metodo, chamado falar que imprime uma msg com o nome da pessoa
class Pessoa:
    def falar(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"Olá, {nome}!")

falar = Pessoa()
falar.falar("uictor", 20)