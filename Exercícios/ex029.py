v = float(input('Qual é a velocidade do carro? '))

if v <= 80:
    print('Tudo dentro da normalidade')
else:
    m = v - 80
    p = m * 7
    print('\nEste veiculo está acima da velocidade permitida'
          '\nA multa por km/h acima do permitido é de R$ 7,00'
          '\nComo passou {} km/h do permitido, a multa será de {}'.format(m, p))