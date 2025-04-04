# Função principal do programa
def main():
    # Lê um número inteiro do usuário
    try:
        numero = int(input("Digite um número inteiro de 1 a 10: "))
        
        # Verifica se o número está no intervalo válido
        if 1 <= numero <= 10:
            # Loop para gerar todos os pares (i, j)
            for i in range(1, numero + 1):
                for j in range(1, numero + 1):
                    soma = i + j
                    print(f"Par (i, j): ({i}, {j}) - Soma: {soma}")
        else:
            print("Número inválido!")
    except ValueError:
        print("Número inválido!")

# Chama a função principal
if __name__ == "__main__":
    main()

