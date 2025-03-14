quantitade = 0
soma = 0
for i in range(80):
    nota = int(input(f"Digite as notas {i + 1} (0 a 10): "))
    if 0 <= nota <=10:
        if nota >= 6:
            quantitade = quantitade + 1
            soma = soma + nota
media = soma/quantitade
print("Qauntidade de alunos aprovados: ", quantitade)
print("Média da turma: ", media)
    
        