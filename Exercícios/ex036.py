from time import sleep

print('\033[33m*-\033[m' * 30)
print('\033[34mBem Vindo!\033[m'
      '\nSomos o Banco JVS'
      '\n>>Preencha os campos abaixo para analisarmos sua condição de emprétimo: ')
print('\033[33m*-\033[m' * 30)
sleep(3)
print('Escolha as opções de empréstimo:'
      '\n1 - Casa (Moradia)')
c = int(input('\nDigite sua opção: '))

if c != 1:
    print('Não Fazemos esse tipo de empréstimo')
elif c == 1:
    print('Ótimo! Vamos ver suas condições: ')
    v = float(input('Qual o valor da casa? '))
    s = float(input('Qual o valor do seu salário? '))
    a = int(input('Em quantos anos você quer parcelar? '))

    p = v / (a * 12)
    if p > (s * 0.3):
        print('\033[31mNão podemos te emprestar\033[m as parcelas ficariam em'
              ' \033[31mR${:.2f}\033[m, que ultrapassa 30% do seu salário'.format(p))
    else:
        print('Parabéns você conseguiu o empréstimo, suas parcelas ficaram em R${:.2f}'.format(p))
