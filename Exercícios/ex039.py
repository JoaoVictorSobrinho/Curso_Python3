from datetime import date
a = int(input('Em qual ano vc nasceu? '))
at = date.today().year

if (at - a) < 18:
    print('Ainda não é o momento de se alistar faltam {} anos'.format(18 - (at - a)))
elif (at - a) == 18:
    print('Está no momento de se alistar, procure uma Junta Militar')
else:
    print('Já passou {} anos do ano de se alistar, você agora é refratário. Procure uma Junta Militar'.format((at - a) - 18))
