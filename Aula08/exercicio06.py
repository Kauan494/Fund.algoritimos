lista = []

qtd = int(input('Digite a qntd de números: '))
for i in range(qtd):
    num = int(input('Digite um número: '))
    lista.append(num)
for i in range(2, len(lista)):
    if lista[i] > (lista[i-1] + lista[i-2]):
        print(lista[i])