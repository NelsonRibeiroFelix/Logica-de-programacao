# 5
print("Digite o valor inicial para a sequência decrescente:")
valor_inicial = int(input())
sequencia_decrescente = []
contador_decrescente = 0
for numero in range(valor_inicial, -1, -1):
    sequencia_decrescente.append(numero)
    contador_decrescente += 1
print("Sequência:", sequencia_decrescente)
print("Quantidade de valores:", contador_decrescente)