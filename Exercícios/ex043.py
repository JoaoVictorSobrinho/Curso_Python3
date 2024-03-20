p = float(input('Seu peso kilos? '))
a = float(input('Sua Altura em metros? '))

imc = p / pow(a, 2)

if imc <= 18.5:
    print('{:.1f}, Abaixo do Peso'.format(imc))
elif 18.5 < imc <= 25:
    print(('{:.1f}, Peso Ideal'.format(imc)))
elif 25 < imc <= 30:
    print('{:.1f}, Sobrepeso'.format(imc))
elif 30 < imc <= 40:
    print('{:.1f}, Obesidade'.format(imc))
else:
    print('{:.1f}, Obesidade Morbida'.format(imc))