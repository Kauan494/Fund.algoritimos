def datamagica(dia,mes,ano):
    ano2dig = ano % 100
    multi = dia * mes
    if ano2dig == multi:
        return True
    else:
        return False
d = int(input('Digite a data: '))
m = int(input('Digite o mês: '))
a = int(input('Digite o ano: '))
if datamagica(d,m,a):
    print(f'{d}/{m}/{a} É uma data mágica!')
else:
    print(f'{d}/{m}/{a} Não é uma data mágica!')
