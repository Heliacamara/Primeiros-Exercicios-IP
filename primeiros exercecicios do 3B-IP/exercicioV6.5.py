# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.5

import random

numero_secreto = random.randint(1, 100)


palpite = None
tentativas = 0

while palpite != numero_secreto:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < 1 or palpite > 100:
            print(" Jogada inválida! Digite um número entre 1 e 100.")
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR que seu palpite.\n")
        elif palpite > numero_secreto:
            print("O número secreto é MENOR que seu palpite.\n")
    except ValueError:
        print("Numero inválido! Digite um número inteiro.\n")

print(f" Você acertou o número secreto: {numero_secreto}")
print(f"Você acertou em {tentativas} tentativas.")