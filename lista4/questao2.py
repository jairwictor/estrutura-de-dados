def customizar(vetor, reverse=False):
    return sorted(vetor, reverse=reverse)


vetor = [90, 100, 32, 13, 15, 40]
vetor_ordenado = customizar(vetor)
print("Vetor ordenado em ordem crescente:", vetor_ordenado)

vetor_ordenadoDecrescente = customizar(vetor, reverse=True)
print("Vetor ordenado em ordem decrescente:", vetor_ordenadoDecrescente)