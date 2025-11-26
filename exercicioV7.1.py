# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V7.1

from string import ascii_lowercase

#begin_inputs
letras = ['z', 'f', 'd', 'n', 'b', 'w', 'r']
#end_inputs

def letras_voluntarias(letras):
    disponiveis = [l for l in ascii_lowercase if l not in letras]
    return disponiveis

print(letras_voluntarias(letras))