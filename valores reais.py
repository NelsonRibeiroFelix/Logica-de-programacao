valores = []  # Lista para guardar os números
quantidade = 0
soma = 0
maiores_que_20 = 0

while True:
    entrada = input("Digite um número (ou 'fim' para terminar): ")
    
    if entrada == 'fim':
        break  # Sai do loop se digitar 'fim'
    
    numero = float(entrada) # Transforma o texto em número
    valores.append(numero)  # Adiciona o número à lista
    quantidade = quantidade + 1
    soma = soma + numero  # Soma os valores
    
    if numero > 20:
        maiores_que_20 = maiores_que_20 + 1

if quantidade > 0:
  media = soma / quantidade
else:
  media = 0

print("Quantidade de números:", quantidade)
print("Soma dos números:", soma)
print("Média dos números:", media)
print("Números maiores que 20:", maiores_que_20)