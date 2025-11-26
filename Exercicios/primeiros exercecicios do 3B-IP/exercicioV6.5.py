# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.5

import random

adivinhar = random.randint(1, 100)
tentativas = 0

while True:
    try:
        tentar = int(input("Digite seu palpite: "))
        tentativas += 1

        if not 1 <= tentar <= 100:
            print("Numero invalido,digite entre 1 e 100.")
            continue

        if tentar == adivinhar:
            print(f"Voce acertou, o numero era {adivinhar}.")
            print(f"Tentativas: {tentativas}")
            break
        elif tentar < adivinhar:
            print("O numero secreto e MAIOR")
        else:
            print("O numero secreto e MENOR")

    except ValueError:
        print("Digite um numero inteiro")
