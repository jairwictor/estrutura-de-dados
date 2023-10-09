print("Calculador de média:")


nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))
nota3 = int(input("Digite a terceira nota do aluno: "))
nota4 = int(input("Digite a quarta nota do aluno: "))
nota5 = int(input("Digite a quintaa nota do aluno: "))


media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if (media < 7):
    print("O aluno está reprovado! ;-;")
elif (media >= 7):
    print("O aluno está aprovado! ;)")