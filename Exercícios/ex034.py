s = float(input('Qual é o seu salário? '))

if s > 1250:
    print('Seu salário com o aumento de 10% é R${:.2f}'.format(s + (s * 0.1)))
else:
    print('Seu salário com aumento de 15% é R${:.2f}'.format(s + (s * 0.15)))
