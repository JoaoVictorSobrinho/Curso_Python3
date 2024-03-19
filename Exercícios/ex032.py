from datetime import date

ano = int(input('Digite algum ano que vc queira (digte 0 para saber o ano atual):  '))
# Nesse caso são três condições (ano divisível por 4 q não seja divisível por 100)
# ou ano q seja divisível por 400
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano de {} É bissexto'.format(ano))
else:
    print('Ano de {} Não é bissexto'.format(ano))