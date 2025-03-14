# Função para calcular a soma S
def calcular_soma(n):
    soma = 0
    for i in range(1, n + 1):
        soma += 1 / i
    return soma

# Leitura do valor de n
n = int(input("Digite um valor inteiro e positivo para n: "))

# Verifica se n é positivo
if n <= 0:
    print("Por favor, digite um valor inteiro e positivo.")
else:
    resultado = calcular_soma(n)
    print(f"A soma S = 1 + 1/2 + 1/3 + ... + 1/{n} é: {resultado:.6f}")


