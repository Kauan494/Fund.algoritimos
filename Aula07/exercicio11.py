def exibir_valores(I, A, B, C):
    if I == 1:
        print(f"A: {A}, B: {B}, C: {C}")
    elif I == 2:
        print(f"B: {C}, C: {B}, A: {A}")
    elif I == 3:
        print(f"C: {A}, A: {C}, B: {B}")
    else:
        print("Valor de I deve ser 1, 2 ou 3.")

# Exemplo de uso da função
exibir_valores(1, 10.5, 20.3, 30.7)
exibir_valores(2, 10.5, 20.3, 30.7)
exibir_valores(3, 10.5, 20.3, 30.7)