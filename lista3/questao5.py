def primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    n = 5
    while n * n <= numero:
        if numero % n == 0 or numero % (n + 2) == 0:
            print("O número não é primo")
        n += 6
    return True

numero =  3
print(f"{numero} {'é' if primo(numero) else 'não é'} primo.")
