from math import sqrt
def calculo(n1,n2,n3):
     return sqrt(n1) +sqrt(n2) + sqrt(n3) + (n1+n2)/2 + (n2+n3)/2 + (n1+n3)/2
a = int(input("Digite o primeiro número: " ))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
print(f'Resultado: ', calculo(a,b,c)) 