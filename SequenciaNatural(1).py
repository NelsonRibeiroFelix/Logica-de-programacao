impares = []
contador_impar = 0
for numero in range(1, 14):
    if numero % 2 != 0:
        impares.append(numero)
        contador_impar += 1
print("Sequência:", impares)
print("Quantidade de números:", contador_impar)