import random  # Importa a biblioteca que gera números aleatórios

linhas = 12     # Define o número de linhas da matriz
colunas = 12    # Define o número de colunas da matriz

matriz = []    # Cria uma lista vazia que vai guardar as linhas (a matriz)
soma = 0 # Variável pra guardar a soma de todos os números
contador = 0    # Variável para contar os números abaixo da diagonal secundária



letra = input('')
if letra == 'S':
    
    print('Matriz criada: ')
elif letra == 'M':
    
    print('Matriz criada:')


# Laço externo: para cada linha
for i in range(linhas):
    linha = []  # Cria uma nova lista para representar a linha atual

    # Laço interno: para cada coluna
    for j in range(colunas):
        # Gera um número aleatório entre 0 e 10
        numero_aleatorio = random.randint(0, 10)

        # Adiciona o número na linha
        linha.append(numero_aleatorio)

          # Se o elemento está abaixo da diagonal secundária (i + j > 11)
        if i + j > 11:
            soma += numero_aleatorio   # Soma os números abaixo da diagonal secundária
            contador += 1              # Conta os números abaixo da diagonal secundária

        

    # Depois que a linha estiver cheia, adiciona ela na matriz
    matriz.append(linha)

# Mostra a matriz na tela, uma linha por vez
for linha in matriz:
     for numero in linha:
        print("%3d" % numero, end=" ") #garante que cada número ocupe 3 espaços de largura, o que faz parecer que tem espaçamento certinho entre eles!
         #o end="" faz com que os números fiquem na mesma linha e separados um pouco    
     print()  # Pula pra próxima linha

if letra == 'S':
    print('Resultado da conta', soma)
elif letra == 'M':
     media = soma // contador  # Média inteira
     print(f'Resultado da conta: {media}')






    







