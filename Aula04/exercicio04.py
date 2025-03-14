anonasc = int(input("Digite seu ano de nascimento: "))
anoatual = int(input("Digite o ano atual: "))
idade = (anoatual-anonasc)
if idade > 16 or idade == 16:
    print("Pode votar!")
else:
    print("Não pode votar!")
if idade > 18 or idade == 18:
    print("Pode tirar a CNH!")
else:
    print("Não pode tirar CNH!")
