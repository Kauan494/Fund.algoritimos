anoatual = int(input("Escreva o ano atual:"))
anonasc = int(input("Escreva o seu ano de nascimento:"))

idade = (anoatual - anonasc)

if idade >= 18:
    print("Você já pode tirar CNH!")
else:
    print("Você ainda não pode tirar CNH!")