t = [11,7,2,4]
menor = 99999999 # usado de valor referencia para comparar com os valores da lista 

for idx in range(len(t)):
    if t[idx] < menor:
        menor = t[idx]
print(t)
print('Menor: ', menor)