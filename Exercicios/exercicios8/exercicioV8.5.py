# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V8.5

contatos = "text85.txt"

def add(nome, tele):
    with open(contatos, "a") as escreva:
        escreva.write(f"{nome} {tele}\n")

def check(contatos):
    with open(contatos, "r") as leia:
        telefones = leia.readlines()
        for contato in telefones:
            print(contato.strip())

print("1 - Adicionar Contato")
print("2 - Ver Contatos")
print("3 - Sair")
pergunta = input("O que voce quer fazer? ")

while pergunta != "3":
    if pergunta == "1":
        nome = input("Nome: ")
        tele = input("Número: ")
        add(nome, tele)
    elif pergunta == "2":
        check(contatos)
    else:
        print("Escolha nao identificada")
    pergunta = input("O que voce quer fazer? ")
