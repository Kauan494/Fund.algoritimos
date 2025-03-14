soma = 0
quantidade = 0
while True:
    numero = int(input("Digite um número ou o 0 para fazer a soma: "))
    if numero == 0:
        break
    soma += numero#abreviasão da conta: soma= numero + soma
    quantidade = quantidade + 1
    media = soma/quantidade
print("A soma é: ", soma)
print("A quantidade de números é de: ", quantidade)
print(f"A média é: {media:.2f}")


     
   
