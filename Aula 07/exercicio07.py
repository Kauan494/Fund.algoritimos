def podedoar(genero,peso):
    if(genero == 'F' and peso >= 50) or (genero == 'M' and peso >= 60):
        return True
    else:
        return False
g = input('Informe o genêro (F/M): ')
p = int(input("Informe o peso: "))

if podedoar(g,p):
    print('Pode doar sangue!')
else:
    print('Não pode doar sangue!')
