# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V6.2


#begin_inputs
n = int(input("Digite um valor:"))
#end_inputs
for h in range(1, n + 1):
    for l in range(1, h + 1):
        print(l, end=" ")
    print()