def media(lista):
    if not lista:  # Verifica se a lista está vazia
        return 0  # Retorna 0 se a lista estiver vazia
    
    soma = sum(lista)  # Calcula a soma dos elementos da lista
    quantidade = len(lista)  # Obtém a quantidade de elementos na lista
    return soma / quantidade  # Retorna a média

# Exemplo de uso da função
print(media([5, 12, 15, 8]))  # Saída: 10.0


