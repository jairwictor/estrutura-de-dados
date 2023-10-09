def soma(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10  
        soma += digito      
        numero //= 10      
    return soma



num = int(input("Digite um número inteiro positivo: "))
if num < 0:
        print("Por favor, digite um número inteiro positivo.")
else:
    resultado = soma(num)
    print(f"A soma dos dígitos de {num} é {resultado}.")

