valor = float(input("Digite o valor da compra: "))
parcelas = float(input("Digite a quantidade de parcelas: "))

desconto_vista= valor * 0.10

valor_alto= valor * 0.05

valor_parcela= valor/parcelas

desconto_parcela= valor * 0.05

desconto_total = float(desconto_vista + valor_alto + desconto_parcela/ valor)

valor_desconto = float(valor - desconto_total)

if valor > 5000 :
    valor_alto= valor * 0.05
    print(f"Desconto total: {desconto_total:.2f}")
    print(f"Valor final da compra com desconto: {valor_desconto:.2f}")
    print(f"Cada parcela será de: {valor_parcela:.2f}")
    desconto_total = float(desconto_vista+valor_alto+desconto_parcela)
    valor_desconto = float(desconto_total - valor)
elif parcelas == 2 or parcelas == 3:
    desconto_parcela= valor * 0.05
    print(f"Desconto total: {desconto_total:.2f}")
    print(f"Valor final da compra com desconto: {valor_desconto:.2f}")
    print(f"Cada parcela será de: {valor_parcela:.2f}")
    desconto_total = float(desconto_vista+valor_alto+desconto_parcela)
    valor_desconto = float(desconto_total - valor)
elif parcelas > 3:
    print("Sem desconto")



    




