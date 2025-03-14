t = int(input("Informe o total de linhas e colunas: "))

for linha in range(t):
    for coluna in range(t):
        if linha % 2 == 0:
            if coluna % 2 == 0:
                print("0", end='')
            else:
                print("*", end='')
        else:
            if coluna % 2 == 0:
                print("*",end='')
            else:
                print("0",end='')
    print()

