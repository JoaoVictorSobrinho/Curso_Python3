n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

m = (n1 + n2) / 2

if m > 6.9:
    print(m)
    print('Parabéns, vc passou!')
elif 5 < m <= 6.9:
    print(m)
    print('Você está de recuperação')
else:
    print(m)
    print('BOMBOU')