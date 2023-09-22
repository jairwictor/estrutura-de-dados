#crie uma classe chamada livro que tenha atributos de titulo e autor.
#implemente um metodo chamado detalhes que retorna umas string com as informações do livro
class livro():

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_detalhes(self):
        print('O título do livro é ',self.titulo,' e o nome do/a autor/a é ', self.autor)

livro1 = livro('Jogos Vorazes', 'Suzane Collins')
livro1.exibir_detalhes()
