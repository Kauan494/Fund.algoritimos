def multiplo(x,y):
    if x % y == 0:
        return True
    else:
        return False
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
if multiplo(n1,n2):
    print('São multiplos!')
else:
    print('Não são múltiplos!')