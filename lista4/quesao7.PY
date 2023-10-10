def terceiro_maiorNumero(vetor):
    if len(vetor) < 3:
        return None

    primeiro_maior = float('-inf')
    segundo_maior = float('-inf')
    terceiro_maior = float('-inf')

    for numero in vetor:
        if numero > primeiro_maior:
            terceiro_maior = segundo_maior
            segundo_maior = primeiro_maior
            primeiro_maior = numero
        elif numero > segundo_maior and numero != primeiro_maior:
            terceiro_maior = segundo_maior
            segundo_maior = numero
        elif numero > terceiro_maior and numero != primeiro_maior and numero != segundo_maior:
            terceiro_maior = numero

    if terceiro_maior == float('-inf'):
        return None

    return terceiro_maior

vetor = [90, 100, 32, 13, 15, 40]
terceiro_maior = terceiro_maiorNumero(vetor)
if terceiro_maior is not None:
    print("Terceiro maior número:", terceiro_maior)
else:
    print("Não há terceiro maior número no vetor.")