
# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.6

import random

def sorteio():
    numesorteado = random.randint(1, 1000)
    trys = 0
    while True:
        palpite = int(input("Digite um numero entre 1 e 1000: "))
        trys += 1
        if trys >= 10:
            print("acabou suas tentativas")
            break

        if palpite < numesorteado:
            print("O numero secreto e MAIOR.")
        elif palpite > numesorteado:
            print("O numero secreto e MENOR.")
        else:
            print(f"Voce acertou,o numero secreto era {numesorteado}.")
            break
       
sorteio()