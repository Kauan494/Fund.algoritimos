# Inicializa a variável para armazenar o número
numero = -1  # Um valor inicial fora do intervalo válido

# Loop que continua até que um número válido seja fornecido
while numero < 0 or numero > 10:
    # Solicita ao usuário um número
    numero = int(input("Digite um número entre 0 e 10: "))
    
    # Verifica se o número está fora do intervalo
    if numero < 0 or numero > 10:
        print("Erro: O número deve estar entre 0 e 10. Tente novamente.")

# Quando um número válido é fornecido
print("Número aceito.")

