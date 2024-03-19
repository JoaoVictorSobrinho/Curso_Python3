print('Digite o valor dos lados do triângulo')
a = float(input('Primeiro Lado: '))
b = float(input('Segundo Lado: '))
c = float(input('Terceiro Lado: '))

if a < b + c and b < c + a and c < b + a:
    print('Triângulo com os lados {}, {}, {} pode ser criado'.format(a, b, c))
else:
    print('Triangulo com os lados {}, {}, {} NÂO pode ser criado'.format(a, b, c))
