from random import randint, random
lista1 = []
lista2 = []
lista3 = ['a','b','c','d','e','f','g']
listacompleta = []

for i in range(10):
    lista1.append(randint(0,10))
for i in range(5):
    lista2.append(random()*10)

listacompleta = lista1 + lista2 + lista3
print(listacompleta)