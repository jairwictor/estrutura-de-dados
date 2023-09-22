#crie uma classe chamada aluno com atributos de nome e notas.
#implemente um metodo calacular_media que retorna a media das notas do aluno
class aluno:
    def calcular_media(self, nome, nota1, nota2, nota3)
        media=(nota1+nota2+nota3) / 3
        if media >= 7:
            print(f'o aluno {nome} está aprovado, sua média foi {media} ')
            
        else:
            print(f'o aluno {nome} está reprovado, sua média foi {media}')

        return media

aluno1=aluno()
aluno1.calcular_media('uictor', 7, 8, 9)
