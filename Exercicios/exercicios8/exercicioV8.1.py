# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V8.1

def escreva_arquivo(arquivo):
    with open(arquivo, "a") as ar:
        ar.write(input("Digite uma frase:" +("\n")))

def ler_arquivo(arquivo):
    with open(arquivo, "r") as f:
        for linha in f:
         print(linha.strip())

print("1-Escrever uma frase")
print("2-Ler e imprimir")

escolha = input("O que voce quer fazer?")

arquivo = "text81.txt"

if escolha == "1":
    escreva_arquivo(arquivo)
else:
    ler_arquivo(arquivo)
