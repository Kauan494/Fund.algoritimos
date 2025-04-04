# Criar uma lista para armazenar as palavras
palavras = []

# Ler palavras do usuário até que uma linha em branco seja inserida
while True:
    palavra = input("Digite uma palavra : ")
    if palavra == "":
        break  
    if palavra not in palavras:#verifica se a 'palavra' está presente na lista 
        palavras.append(palavra)
print('Palavras digitadas: ')
for palavra in palavras:
    print(palavra)