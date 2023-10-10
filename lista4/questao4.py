def segundo_menorNum(vetor):
    if len(vetor) < 2:
        return None

    menor = float('inf')
    segundo_menor = float('inf')

    for numero in vetor:
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif numero < segundo_menor and numero != menor:
            segundo_menor = numero

    if segundo_menor == float('inf'):
        return None

    return segundo_menor

vetor = [90, 100, 32, 13, 15, 40]
segundo_menor = segundo_menorNum(vetor)
if segundo_menor is not None:
    print("Segundo menor número:", segundo_menor)
else:
    print("Não há segundo menor número no vetor.")