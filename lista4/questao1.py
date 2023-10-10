def ordenar_vetor(vetor):
    n = len(vetor)

    for i in range(n):
        min_vetor = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[min_vetor]:
                min_vetor = j
        vetor[i], vetor[min_vetor] = vetor[min_vetor], vetor[i]

vetor = [90, 100, 32, 13, 15, 40]
ordenar_vetor(vetor)
print("Vetor ordenado:", vetor)