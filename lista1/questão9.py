nomes = ["Aline", "vitor", "Paulo", "Ana", "Alicia", "Marcos", "Mariana", "Amanda"]
com_A = []
sem_A = []

for i in nomes:
    if i[0] == "A":
        com_A.append(i)
    else:
        sem_A.append(i)


print(com_A)