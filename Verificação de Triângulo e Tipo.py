def tipo_triangulo(a, b, c):

  if a < b + c and b < a + c and c < a + b:
    if a == b == c:
      return "Triângulo equilátero"
    elif a == b or a == c or b == c:
      return "Triângulo isósceles"
    else:
      return "Triângulo escaleno"
  else:
    return "Não é um triângulo"

# Exemplos de uso
print(tipo_triangulo(1, 2, 3))  # Não é um triângulo
print(tipo_triangulo(2, 3, 4))  # Triângulo escaleno
print(tipo_triangulo(3, 3, 3))  # Triângulo equilátero
print(tipo_triangulo(2, 3, 3))  # Triângulo isósceles