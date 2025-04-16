soma_pares = 0
quantidade_pares = 0
soma_impares = 0
quantidade_impares = 0

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break
    
    if numero % 2 == 0:  # Verifica se o número é par
        soma_pares += numero
        quantidade_pares += 1
    else:  # Se não for par, é ímpar
        soma_impares += numero
        quantidade_impares += 1

if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print("Média dos números pares:", media_pares)
else:
    print("Nenhum número par foi digitado.")

if quantidade_impares > 0:
    media_impares = soma_impares / quantidade_impares
    print("Média dos números ímpares:", media_impares)
else:
    print("Nenhum número ímpar foi digitado.")