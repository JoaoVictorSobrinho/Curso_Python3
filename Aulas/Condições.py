# Estrutura sequencial vs condicional

# Estrurura sequencial: Pensamento contínuo (Linha reta)
# Estrutura condicional: Pensamento por ramificações

"""if carro.esquerda():
    bloco True
else:
    bloco False """


tempo = int(input('Quantos anos seu carro tem? '))
# Condição
if tempo <= 3:
    print('carro novo')
# if 5 >= tempo or tempo > 3:
#    print('carro usado')
else:
    print('carro usado')

# Condição Simplificada
# print('carro novo' if tempo <= 3 else 'carro velho')


n1 = float(input('Qual é a primeira nota? '))
n2 = float(input('Qual é a segunda nota? '))

m = (n1 + n2) / 2
print('Sua média foi {}'.format(m))
if m >= 6:
    print('Sua média foi suficiente')
else:
    print('Sua média não foi suficiente')
