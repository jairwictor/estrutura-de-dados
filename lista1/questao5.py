
pares = []

num = int(input("Digite um numero: "))
for i in range(2, num, 2):
    pares.append(i)

soma = sum(pares)
quantidade = len(pares)

media = soma / quantidade

print(pares)
print(media)
