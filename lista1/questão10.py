from random import randint
itens = ("Pedra", "Papel", "Tesoura")
pc = randint(0,2)
escolha_pc = itens[pc]

print("Suas opções: 0 > Pedra, 1 > Papel, 2 > Tesoura")

opcao = int(input("Digite o valor de sua opção: "))
escolha = itens[opcao]


if escolha_pc == escolha:
    print("Empate!")
elif escolha_pc == "Pedra" and escolha == "Papel":
    print("Voce ganhou!")
elif escolha_pc == "Pedra" and escolha == "Tesoura":
    print("Voce perdeu")
elif escolha_pc == "Papel" and escolha == "Pedra":
    print("Voce perdeu")
elif escolha_pc == "Papel" and escolha == "Tesoura":
    print("Voce ganhou")
elif escolha_pc == "Tesoura" and escolha == "Pedra":
    print("Voce ganhou")
elif escolha_pc == "Tesoura" and escolha == "Papel":
    print("Voce perdeu!")

print(f"Voce escolheu {escolha}")
print(f"O pc escolheu {escolha_pc}")
