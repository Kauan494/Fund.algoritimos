lista = []
maior = -9999999 # usado de valor referencia para comparar com os valores da lista 
for i in range(10):
     num = float(input(f'Digite um valor {i}: '))
     lista.append(num)
     if lista[i] > maior:
          maior = lista[i]
          i_maior = i 
print('Números:',lista)
print('Maior número: ', maior)
print('Indice maior: ',i_maior)


