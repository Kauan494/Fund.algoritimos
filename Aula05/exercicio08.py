x = 0
soma = 0
while True:
    numero = int(input("Digite um número ou o 0 para fazer a soma: "))
    if numero == 0:
        break
    soma = soma + numero
print("Soma:",soma)