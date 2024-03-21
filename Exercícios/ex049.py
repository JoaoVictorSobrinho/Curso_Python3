n = int(input('Digite o valor da tabuada: '))
m = int(input('Digite o multiplo da tabuada: '))
for t in range(1, n + 1):
    print('{} x {} = {}'.format(m, t, (t * m)))
