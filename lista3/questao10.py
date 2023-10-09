def seq_Fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

num_termo = int(input("Digite o número desejado para ver a sequência Fibonacci: "))

resultado = seq_Fibonacci(num_termo)

print(resultado)