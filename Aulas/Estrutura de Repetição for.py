# Serve para situações que um mesmo comando se repete
# laço

# laço c no intervalo(1, 10)
#      passo
# pega

# for c in range(1, 10):
#     if moeda:
#         pega
#     passo
# pega

for o in range(1, 5, 2):
    if o != 2 and o != 6:
        print('Olá')
    else:
        print('Oi')

n = int(input('Digite um número '))
for c in range(0, n+1):
    print(c)
print('FIM')

s = 0
for k in range(0, 5):
    n = int(input('Digite um número: '))
    s += n
print('Soma é {}'.format(s))
