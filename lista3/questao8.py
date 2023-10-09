print("Digite 1 para calcular Celsius para Fahrenheit")
print("Digite 2 para calcular Fahrenheit para Celsius")

escolha = int(input())

if escolha == 1:
    temperatura = float(input("Digite a temperatura: "))
    resultado = (temperatura * 1.8) + 32
    print(resultado)
elif escolha == 2:
    temperatura = float(input("Digite a temperatura: "))
    resultado = (temperatura - 32) / 1.8
    print(resultado)
else:
    print("Digite um valor valido!")