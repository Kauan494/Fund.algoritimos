def area(base,altura):
    return (base*altura)/2
while(True):
    b = int(input("Informe a base: "))
    a = int(input("Informe a altura: "))
    print("Área do triângulo: ", area(b,a))

    continua =  input("Quer calcular a área de mais de um triângulo? ")

    if continua != 'S':
        break