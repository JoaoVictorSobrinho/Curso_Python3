from datetime import date
a = int(input('Em que ano o aluno nasceu? '))
ano = date.today().year
idade = ano - a

if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
