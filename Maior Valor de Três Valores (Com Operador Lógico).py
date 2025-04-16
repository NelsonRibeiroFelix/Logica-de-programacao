def maior_valor_com_logica(valor1, valor2, valor3):

  if valor1 >= valor2 and valor1 >= valor3:
    return valor1
  elif valor2 >= valor1 and valor2 >= valor3:
    return valor2
  else:
    return valor3


valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

maior = maior_valor_com_logica(valor1, valor2, valor3)
print(f"O maior valor é: {maior}")