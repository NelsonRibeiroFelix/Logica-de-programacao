aprovados = 0
reprovados = 0
total_alunos = 0

while True:
    nota = input("Digite a nota do aluno (ou 'fim' para terminar): ")
    
    if nota == 'fim':
        break
    
    nota = float(nota)
    total_alunos += 1
    
    if nota >= 5:
        aprovados += 1
    else:
        reprovados += 1

print("Quantidade de alunos que fizeram a prova:", total_alunos)
print("Quantidade de alunos aprovados:", aprovados)
print("Quantidade de alunos reprovados:", reprovados)