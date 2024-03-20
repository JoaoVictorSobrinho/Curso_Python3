n1 = int(input('Digite o Primeiro Numero: '))
n2 = int(input('Digite o Segundo Numero: '))

if n1 > n2:
    print('{} é o maior!'.format(n1))
elif n1 < n2:
    print('{} é o maior!'.format(n2))
else:
    print('Não tem maior')
