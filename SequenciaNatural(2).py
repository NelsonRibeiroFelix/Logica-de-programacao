multiplos_de_3 = []
soma_multiplos_de_3 = 0
for numero in range(1, 22):
    if numero % 3 == 0:
        multiplos_de_3.append(numero)
        soma_multiplos_de_3 += numero
print("Sequência:", multiplos_de_3)
print("Soma dos números:", soma_multiplos_de_3)