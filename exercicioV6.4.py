# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.4


#begin_inputs

#end_inputs

valores = list(map(int, input("Jogadas: ").split()))

jogadas = valores[0]

if jogadas in [7, 11]:
    print("Você tirou um natural (7 ou 11)!")
    print("Você ganhou!")
elif jogadas in [2, 3, 12]:
    print("Você tirou um craps (2, 3 ou 12)!")
    print("Você perdeu!")
else:
    numero = jogadas
    print(f"Seu ponto é {numero}. Continue jogando até tirar {numero} novamente (ou 7 para perder).")

    for valor in valores[1:]:
        if valor == numero:
            print("Você tirou seu ponto novamente!")
            print("Você ganhou!")
            break
        elif valor == 7:
            print("Você tirou 7 antes do ponto!")
            print("Você perdeu!")
            break
    else:
        print("O jogo terminou sem resultado (faltaram jogadas).")