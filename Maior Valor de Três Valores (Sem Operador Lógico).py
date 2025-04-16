def maior_valor_sem_logica(valor1, valor2, valor3):

  maior = valor1
  if valor2 > maior:
    maior = valor2
  if valor3 > maior:
    maior = valor3
  return maior


valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

maior = maior_valor_sem_logica(valor1, valor2, valor3)
print(f"O maior valor é: {maior}")