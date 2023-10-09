def palindromo(word):
    esquerda = 0
    direita = len(word) - 1

    while esquerda < direita:
        if word[esquerda] != word[direita]:
            return False
        esquerda += 1
        direita -= 1
        return True


pali = "subi no onibus"

if palindromo(pali):
    print(f"{pali} é um palíndromo.")
else:
    print(f"{pali} não é um palíndromo.")
