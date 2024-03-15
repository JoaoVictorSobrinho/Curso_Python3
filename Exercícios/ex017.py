import math

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))

hi = math.hypot(co, ca)
hi2 = math.sqrt(pow(co, 2) + pow(ca, 2))
hi3 = (((co ** 2) + (ca ** 2)) ** (1/2))

print('O valor direto: {}\n'
      'O valor calculado: {} e {}'.format(hi, hi2, hi3))

