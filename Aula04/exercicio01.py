preco =int(input("Preço do produto:"))
codigo = int(input("Código de origem:")) 

if codigo == 1:
    print("Sul")
elif codigo == 2:
    print("Norte")
elif codigo == 3:
    print("Leste")
elif codigo == 4:
    print("Oeste")
elif (codigo == 5) or (codigo == 6):
    print("Nordeste")
elif (codigo == 7) or (codigo == 8) or (codigo == 9):
    print("Sudeste")
elif (codigo >= 10 and codigo <= 20):
    print("Centro-Oeste")
elif (codigo >=25 and codigo <= 30):
    print("Nordeste")
else:
    print("O produto é importado")
    
