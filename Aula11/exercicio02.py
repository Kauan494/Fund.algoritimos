import random  # importa a biblioteca para gerar números aleatórios

# Cria um dicionário vazio onde a chave será o número e o valor será a quantidade de vezes que apareceu
contagem = {}

# Gera 100 números aleatórios entre 0 e 20
for _ in range(100):
    numero = random.randint(0, 20)  # gera um número entre 0 e 20

    # Se o número já está no dicionário, aumenta a contagem
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1  # Se for a primeira vez, coloca 1

print(contagem)




