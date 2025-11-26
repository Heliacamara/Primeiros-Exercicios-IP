# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.4


#begin_inputs

#end_inputs
primeira_soma = int(input("Digite um numero: "))

if primeira_soma in (7, 11):
    print("Voce ganhou!")
elif primeira_soma in (2, 3, 12):
    print("Voce perdeu!")
else:
    ponto_alvo = primeira_soma

    while True:
        try:
            nova_soma = int(input("Digite outro numero: "))
        except:
            break

        if nova_soma == ponto_alvo:
            print("Voce ganhou!")
            break
        elif nova_soma == 7:
            print("Voce perdeu!")
            break
