h = float(input('Qual é a Altura da parede? '))
b = float(input('Qual é a Largura da parede? '))

a = h * b
i = a / 2

print('\nPara uma parede com dimensões {}m de altura e {}m de largura.\n'
      'A área da parede é de {:.4}m².\n'
      'A quantidade de Tinta necessária para pintar essa parede será {:.4}L.\n'
      'Considerando que cada litro pinta uma área de 2m²'.format(h, b, a, i))
