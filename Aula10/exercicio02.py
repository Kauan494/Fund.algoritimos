from random import randint, random
M = []

for linha in range(10):
    M_inteira = []
    for coluna in range(15):
        M_inteira.append(randint(0,10))
    M.append(M_inteira)
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print("%4d" %M[linha][coluna], end= '')
    print()
for linha in range(len(M)):
    print("%4d" %M[linha][0])
