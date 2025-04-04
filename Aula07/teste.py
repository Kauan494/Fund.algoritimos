def maximo(x, y, imprime=False):
    # Determina o maior valor
    if x > y:
        maior = x
    else:
        maior = y
    
    # Se imprime for True, imprime o valor máximo
    if imprime:
        print('Maior:', maior)
    
    # Retorna o maior valor e os outros parâmetros
    return maior, x, y

# Chama a função sem imprimir
resultado = maximo(1, 2)
print("Resultado sem imprimir:", resultado)

# Chama a função com imprime como True
resultado = maximo(1, 2, imprime=True)
print("Resultado com imprimir:", resultado)