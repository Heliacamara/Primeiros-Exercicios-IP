# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V7.1

from string import ascii_lowercase

#begin_inputs
letras = ['a', 'e', 'i']
#end_inputs

def letras_disponiveis(letras):
    disponiveis = [l for l in ascii_lowercase if l not in letras]
    return disponiveis

print(letras_disponiveis(letras))