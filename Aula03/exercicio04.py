a = float(input("Digite o salário do funcionário: R$"))
aumento =(a *0.10)
aumento2 =(a *0.15)
if a > 1250.00:
    novo_salario = a + aumento
elif a <= 1250.00:
   novo_salario = a + aumento2

print("Novo salário é: R$", novo_salario)


