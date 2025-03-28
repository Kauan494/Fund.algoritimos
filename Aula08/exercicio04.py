lista = []
soma = 0
for i in range(10):
    num = float(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        soma+=num
print(lista)
print('Soma dos pares: ',soma)
print('Soma dos indices de pares: ')
