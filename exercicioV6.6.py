
# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.6

import random

import random

def sorteio():
    sorteado = random.randint(1, 1000000)  
    trys = 0  
    limite_tentativas = 6  

    print(f"Voce tem {limite_tentativas} tentativas para acertar o numero entre 1 e 1.000.000.")
    
    while trys < limite_tentativas:  
        try:
            palpite = int(input("Digite um numero entre 1 e 1000000: ")) 
        except ValueError:  
            print("Insira um numero valido.")
            continue
        
        trys += 1  

        if palpite < sorteado:
            print("O numero secreto e MAIOR.")
        elif palpite > sorteado:
            print("O numero secreto e MENOR.")
        else:
            print(f"Parabéns! Voce acertou,o numero secreto era {sorteado}.")
            print(f"Voce acertou em {trys} tentativas!")
            break  

    if trys >= limite_tentativas and palpite != sorteado:  
        print(f"Voce perdeu,o numero secreto era {sorteado}.")

sorteio()
