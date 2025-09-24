n1=int(input("Digite a sua primeira nota:"))
n2=int(input("Digite a sua segunda nota:"))
n3=int(input("Digite a sua terceira nota:"))
n4=int(input("Digite a sua quarta nota:"))

soma= n1+n2+n3+n4/4

média= int(soma)
if média>=60:
    print("Parabéns,você esta aprovado!")
else:
    print("Que pena,você esta reprovado!")