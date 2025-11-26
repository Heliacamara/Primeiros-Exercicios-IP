# @cikey f8a3d76c7a6f58f18a695f0148380a0a
# @sid 20251174010003
# @aid V8.3

with open( "text82.txt","r") as arq1:
    conteudo = arq1.read()
with open("text83.txt","w") as arq2:
    arq2.write(conteudo)
print("Arquivo copiado")