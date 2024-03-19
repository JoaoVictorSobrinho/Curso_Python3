from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 20)
print('Pensei em um valor de 0 a 5, tente adivinhar')
print('-=-' * 20)
c = int(input('Digite seu paplpite: '))
print('Processando...')
sleep(2)
if pc == c:
    print('PARABENS')
else:
    print('TENTE NOVAMENTE')
