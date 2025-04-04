def divisao_inteira(dividendo, divisor):
    # Inicializa o quociente e o resto
    quociente = 0
    resto = dividendo

    # Enquanto o resto for maior ou igual ao divisor
    while resto >= divisor:
        resto -= divisor  # Subtrai o divisor do resto
        quociente += 1    # Incrementa o quociente

    return quociente, resto

# Programa principal
def main():
    # Recebe o dividendo e o divisor do usuário
    dividendo = int(input("Digite o dividendo: "))
    divisor = int(input("Digite o divisor: "))

    # Verifica se o divisor é diferente de zero
    if divisor == 0:
        print("Erro: Divisão por zero não é permitida.")
        return

    # Chama a função de divisão
    quociente, resto = divisao_inteira(dividendo, divisor)

    # Exibe o resultado
    print(f"Quociente: {quociente}, Resto: {resto}")

# Executa o programa principal
if __name__ == "__main__":
    main()
