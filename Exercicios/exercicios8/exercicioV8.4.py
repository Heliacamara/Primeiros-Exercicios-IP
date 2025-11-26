# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V8.4

with open("text84.txt", "w") as arq:
    for _ in range(5):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        arq.write(f"{cpf};{nome}\n")

print("Conteudo do arquivo:")
with open("text84.txt", "r") as arq:
    for linha in arq:
        print(linha.strip())
