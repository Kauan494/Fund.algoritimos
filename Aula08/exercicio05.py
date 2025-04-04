num = int(input('Digite a qtde de números : '))
lista = []
lista1 = lista[:]
for i in range(num):
    num1 = int(input('Digite um número: '))
    lista.append(num1)
    lista1.insert(0,num1)
print('Números: ',lista)
print('Inverso: ',lista1)