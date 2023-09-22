#crie uma classe chamada funcionario com atributos nome, salario e cargo. 
#implemente um método chamado aumentar_salario que recebe um valor percentual de aumento e atualiza o salário do funcionário.

class funcionario:
    def aumentar_salario(self, nome, salario, cargo):
        aumento = salario * 0.5
        salario_atual = salario + aumento
        print(f'O salário do funcionário {nome} obteve o aumento de {aumento} ficando agora no total de {salario_atual} ')

funcionario1 = Funcionario()
funcionario1.aumentar_salario("uictor", 1300, "vendedor")