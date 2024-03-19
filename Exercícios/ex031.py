km = float(input('Qual a distância da viagem? '))

if km <= 200:
    print('O valor da viagem é R$ {:.2f}'.format(km * 0.5))
else:
    print('O valor da viagem é R$ {:.2f}'.format(km * 0.45))