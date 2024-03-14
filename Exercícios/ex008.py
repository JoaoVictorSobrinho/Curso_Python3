m1 = float(input('Qual é a medida em metros? '))

m2 = m1 * 100
m3 = m1 * 1000

print('A medida que você inseriu foi {}m\n'
      'Em centimetros se torna {}cm\n'
      'Em Milimetros se torna {}mm\n'.format(m1, m2, m3))