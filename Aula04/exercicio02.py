a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite outro número: "))

if a > b and a > c:
    if b > c:
        print(f"Ordem decrescente: {a},{b},{c}")
    elif c > b:
        print(f"Ordem decrescente: {a},{c},{b}")
if b > a and b > c:
    if a > c:
        print(f"Ordem decrescente: {b},{a},{c}")
    elif c > a:
        print(f"Ordem decrescente: {b},{c},{a}")
else:
    if c > a and c > b:
        if a > b:
            print(f"Ordem decrescente: {c},{a},{b}")
        elif b > a:
            print(f"Ordem decrescente: {c},{b},{a}")    


