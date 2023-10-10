def removerDuplicatas(vetor):
    elementosUnicos = set()

    vetor_sem_duplicatas = []

    for elemento in vetor:
        if elemento not in elementosUnicos:
            elementosUnicos.add(elemento)
            vetor_sem_duplicatas.append(elemento)
    return vetor_sem_duplicatas

vetor = [90, 100, 32, 13, 15, 40]
vetor_sem_duplicatas = removerDuplicatas(vetor)
print("O vetor sem duplicatas:", vetor_sem_duplicatas)