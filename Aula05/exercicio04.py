x = 0
for i in range(6):
    numero = int(input(f"Digite um número {i + 1}:"))
    if numero > x:
        x = numero
print("Maior número é:",x)
