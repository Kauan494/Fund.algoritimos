quantidade = int(input("Digite a quantitade de números que deseja inserir: "))
cont_primos = 0

for i in range(0,quantidade):
    num =int(input(f"Digite o número {i}:  "))
    if num > 1:
        eh_primo= True
        for j in range(2,num):
            if num % j == 0:
                eh_primo = False
                break
        if eh_primo:
            cont_primos = cont_primos + 1
print(f"Você digitou {cont_primos} números primos de um total de {quantidade} números")
        
