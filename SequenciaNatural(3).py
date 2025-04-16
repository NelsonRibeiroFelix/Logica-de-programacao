dobros = []
soma_dobros = 0
for numero in range(1, 11):
    dobro = numero * 2
    dobros.append(dobro)
    soma_dobros += dobro
print("Sequência:", dobros)
print("Soma dos números:", soma_dobros)
if len(dobros) > 0:
    media_dobros = soma_dobros / len(dobros)
    print("Média aritmética:", media_dobros)