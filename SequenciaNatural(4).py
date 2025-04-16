print("Digite o valor final para a sequência crescente:")
valor_final = int(input())
sequencia_crescente = []
contador_crescente = 0
for numero in range(1, valor_final + 1):
    sequencia_crescente.append(numero)
    contador_crescente += 1
print("Sequência:", sequencia_crescente)
print("Quantidade de valores:", contador_crescente)