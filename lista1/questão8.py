def num_primo(numero):
    if numero < 2:
        return False
    for i in range (2, int(numero ** 0.5) +1):
        if numero % i == 0:
            return False
    return True

num = int(input("Digite um numero: "))

if num_primo(num):
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo!")