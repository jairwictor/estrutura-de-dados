def calculadora(num1,num2,escolha):
    if escolha == 1:
        soma = num1 + num2
        resultado = soma
    elif escolha == 2:
        subtracao = num1 - num2
        resultado = subtracao
    elif escolha == 3:
        dividir = num1 / num2
        resultado = dividir
    elif escolha == 4:
        multiplicacao = num1 * num2
        resultado = multiplicacao
    else:
        resultado = "Valor invalido!"

    return print(resultado)

escolha = int(input("Digite 1 para somar, 2 para subtrair, 3 para dividir e 4 para multiplicar: "))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

calculadora(num1,num2,escolha)