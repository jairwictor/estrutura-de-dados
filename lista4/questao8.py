def calcularMediana(vetor):
    vetor_ordenado = sorted(vetor)
    tamanho = len(vetor_ordenado)

    if tamanho % 2 == 1:
        return vetor_ordenado[tamanho // 2]
    else:
        meio1 = vetor_ordenado[(tamanho // 2) - 1]
        meio2 = vetor_ordenado[tamanho // 2]
        return (meio1 + meio2) / 2.0

vetor = [90, 100, 32, 13, 15, 40]
mediana_valor = calcularMediana(vetor)
print("A mediana é:", mediana_valor)