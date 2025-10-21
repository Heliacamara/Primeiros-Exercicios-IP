# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V7.2


#begin_inputs
letras = ['p', 'e', 'd','r']
palavra= 'pedir'
#end_inputs

def letras_disponiveis(letras,palavra):
    for letra in palavra:
     if letra not in letras:
        return False
    return True

print(letras_disponiveis(letras,palavra))