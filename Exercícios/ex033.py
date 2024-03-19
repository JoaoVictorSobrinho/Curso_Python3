print('-=*=-' * 7)
print('Digite três números diferentes')
print('-=*=-' * 7)
a = int(input('primeiro: '))
b = int(input('segundo: '))
c = int(input('terceiro '))

if a < b and a < c:
    print('Menor valor é {}'.format(a))
if b < a and b < c:
    print('Menor valor é {}'.format(b))
if c < a and c < b:
    print('Menor valor é {}'.format(c))

maior = a
if c > a and c > b:
    maior = c
if b > a and b > c:
    maior = b
print('Maior valor é {}'.format(maior))
