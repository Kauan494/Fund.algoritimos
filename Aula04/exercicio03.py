altura = float(input("Digite sua altura em metros: "))
sexo = str(input("Digite seu sexo: "))
h = (72.7 * altura) - 58
m = (62.1 * altura) - 44.7
if sexo == "homem":
    print(f"Seu peso ideal é: {h:.2f}")
elif sexo == "mulher":
    print(f"Seu peso ideal é:{m:.2f} ")