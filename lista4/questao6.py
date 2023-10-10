def contar_paresEimpares(vetor):
    vetor_ordenado = sorted(vetor, reverse=True)
    pares = 0
    impares = 0

    for numero in vetor_ordenado:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

vetor = [90, 100, 32, 13, 15, 40]
pares, impares = contar_paresEimpares(vetor)

print("Vetor ordenado em ordem decrescente:", vetor)
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)