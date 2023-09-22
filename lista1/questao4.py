lista=[]
maior=0
menor=0
for i in range(0,10):
    lista.append(int(input('Digite um número:')))
    if i==0:
        maior=menor=lista[i]
    else:
        if lista[i]>maior:
            maior=lista[i]
        if lista[i]<menor:
            menor=lista[i]
print('O maior número digitado foi', maior)
print('e o menor número digitado foi', menor)