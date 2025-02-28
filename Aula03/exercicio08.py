from math import ceil, pi


altura = float(input("Digite a altura do cilindro:"))
raio = float(input("Digite o raio do cilindro:"))
tinta = int(input("Digite a a qntd de latas:"))
#Calculo da área do cilindro
area_base = pi * raio
perimetro = 2 * pi * raio
area_lateral = altura * perimetro
area_total = area_base + area_lateral
print("Área a ser pintada: %.2f" % area_total)
#Calcular número de latas
litros_necessarios = area_total / 3
latas_necessarias = litros_necessarios / 5
latas_necessarias = ceil(latas_necessarias)
print("Latas necessárias:", latas_necessarias)
print("Qntd de litros necessarios : %.2f" % litros_necessarios)

#Custo das latas
if tinta == 1:
    custo = tinta * 50.00
elif tinta == 2:
     custo = tinta * 48.00
elif tinta == 3:
   custo = tinta * 46.00
else:
   custo = tinta * 45.00

print("Custo unitário: R$",custo)

custo_total = custo * latas_necessarias
print("Custo tota será de: R$",custo_total)
