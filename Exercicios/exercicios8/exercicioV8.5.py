# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V8.5

contatos = "text85.txt"

def ler():
    with open(contatos,"r") as r:
        nome = input("Nome: ")
        contato = r.readlines()
        for contate in contato:
            print(contate.strip(), "\n")
        else:
            print("Contato nao encontrado\n")

def salvar():
    with open("text85.txt", "w") as arq:
        for nome, tel in contatos.items():
            arq.write(f"{nome};{tel}\n")
    print("Contatos salvos\n")

while True:
    print("1-Ler  2-Salvar  3-Sair")
    op = input("Opcoes: ")

    if op == "1":
        ler()
    elif op == "2":
        salvar()
    elif op == "3":
        break
    else:
        print("Opcao invalida\n")
