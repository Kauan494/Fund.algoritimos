def datamagica(dia,mes,ano):
    ano2dig = ano % 100
    multi = dia * mes
    
    if ano2dig == multi:
         return True
    else:
        return False
for a in range(1901,2001):
    for m in range(1,32):
        for d in range(1,32):
            if datamagica(d,m,a):
                print(f'{d}/{m}/{a} é uma data mágica!')        
 