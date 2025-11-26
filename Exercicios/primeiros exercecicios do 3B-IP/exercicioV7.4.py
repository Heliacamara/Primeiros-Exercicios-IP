# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V7.4

contatos = {}

for i in range(3):
    chave_nome = input("Digite um nome: ")
    valor_tel = input("Digite um telefone: ")
    contatos[chave_nome] = valor_tel

print("Lista de contatos:")
print(contatos)

procura_nome = input("Qual o nome que voce quer consultar:")

if procura_nome in contatos:
    print(f"O telefone de {procura_nome} e {contatos[procura_nome]}")
else:
    print("Contato nao encontrado")
