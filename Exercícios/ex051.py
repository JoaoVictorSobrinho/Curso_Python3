n = float(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))
pr = int(input('Número de repetições: '))
print(n)
for p in range(0, 10):
    n *= r
    print('{}'.format(n))
