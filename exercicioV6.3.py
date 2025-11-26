# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.3


#begin_inputs
n = 127
#end_inputs

def inverte_numero(n):
    s= str (n)
    s_invertido = s [::-1]
    return int (s_invertido)
print(inverte_numero(n))