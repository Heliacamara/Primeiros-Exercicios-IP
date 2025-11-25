# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.2


#begin_inputs
n = int(input("Digite um valor:"))
#end_inputs

def subida(n):
    for i in range(1, n +1):
        for s in range(1, i + 1):
            print(s, end= ' ')
        print()        
subida(n)                