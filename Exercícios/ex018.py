import math

ang = float(input( 'Informe o ângulo desejado: '))

ang1 = math.radians(ang)
s = math.sin(ang1)
c = math.cos(ang1)
t = math.tan(ang1)

print('O ângulo {}, corresponde:\n'
      'Valor de seno {:.2f}\n'
      'Valor de COsseno {:.2f}\n'
      'Valor de Tangente {:.2f}'.format(ang, s, c, t))
