temperaturas = [-10,-8,0,1,2,5,-2,-4]
menor = 99999999
maior = -9999999
for idx in range(len(temperaturas)):
    if temperaturas[idx] < menor:
       menor = temperaturas[idx]

    elif temperaturas[idx] > maior:
            maior = temperaturas[idx]
media = (menor + maior)/2
print(temperaturas)            
print('Menor: ',menor)
print('Maior: ',maior)
print('Média: ',media)