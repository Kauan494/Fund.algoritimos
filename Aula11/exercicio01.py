# Função que procura chaves com um valor específico
def procuraChave(dicionario, valor_procurado):
    resultado = []  # Lista onde vamos guardar as chaves encontradas

    # Percorre todas as chaves do dicionário
    for chave in dicionario:
        # Verifica se o valor associado à chave é igual ao valor procurado
        if dicionario[chave] == valor_procurado:
            resultado.append(chave)  # Se for igual, adiciona a chave na lista

    return resultado  # Retorna a lista de chaves encontradas

# Criação do dicionário com valores numéricos
dicionario = {
    "alpha": 1,
    "bravo": 2,
    "charlie": 1,
    "delta": 3,
    "echo": 1
}
# Pede ao usuário para digitar o valor a ser procurado
valor_digitado = int(input("Procurando chave com valor: "))

# Chama a função e guarda a lista de chaves encontradas
resultado = procuraChave(dicionario, valor_digitado)

# Mostra o resultado para o usuário
print(resultado)




    
  

