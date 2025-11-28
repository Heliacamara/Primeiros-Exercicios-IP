# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.4


#begin_inputs

#end_inputs

dado = int(input("Digite o valor sorteado no dado: "))

if dado == 7 or dado == 11:
    print("Voce ganhou!")

elif dado == 2 or dado == 3 or dado == 12:
    print("Voce perdeu!")

else:
   ponto = dado
   valor_dado = int(input("Digite o valor sorteado no dado: "))
   while True:
        if valor_dado == ponto:
            print("Voce ganhou!")
            break    
        elif valor_dado == 7:
            print("Voce perdeu!")
            break
        else:
            valor_dado = int(input("Digite o valor sorteado no dado: "))