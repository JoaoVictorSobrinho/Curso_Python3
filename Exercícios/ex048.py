s = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        print(c)
        s += c
print('Soma dos Multiplos de 3 é {}'.format(s))
