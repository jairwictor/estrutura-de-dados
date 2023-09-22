def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] + sequencia[-2] <= n:
        num = sequencia[-1] + sequencia[-2]
        sequencia.append(num)
    return sequencia

valor = int(input("Digite um numero limite para a sequência de fibonacci: "))

sequencia_fib = fibonacci(valor)
print("Sequência de fibonacci até", valor, ":", sequencia_fib)