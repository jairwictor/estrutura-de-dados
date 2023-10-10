def encontrar_maximoEminimo(vetor):
    if not vetor:
        return None, None

    maximo = vetor[0]
    minimo = vetor[0]

    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
        elif elemento < minimo:
            minimo = elemento

    return maximo, minimo

vetor = [90, 100, 32, 13, 15, 40]
maximo, minimo = encontrar_maximoEminimo(vetor)
print("Máximo:", maximo)
print("Mínimo:", minimo)