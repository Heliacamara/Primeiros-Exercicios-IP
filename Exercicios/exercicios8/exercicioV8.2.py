# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V8.2

with open("text82.txt", "w+") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
    arquivo.write("Linha 4\n")
    arquivo.write("Linha 5\n")

with open("text82.txt", "r+") as arquivo:
    linhas = arquivo.readlines()
print(f"Quantidade de linhas:{len(linhas)}")
