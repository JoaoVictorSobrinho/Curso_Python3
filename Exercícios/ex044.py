p = float(input('Preço do Produto: '))
print('Formas de Pagamento:'
      '\n1 - Dinheiro'
      '\n2 - Cheque'
      '\n3 - Cartão')
f = int(input('Escolha a forma de pagamento: '))

if f == 1 or f == 2 or f == 3:
    if f == 1 or f == 2:
        print('O valor do produto terá desconto de 10%, e seu valor é: R${:.2f}'.format(p - (p * 0.1)))
    elif f == 3:
        parcela = int(input('Em quantas parcelas? '))
        if parcela == 1:
            print('O valor do produto terá desconto de 5%, e seu valor é: R${:.2f}'.format(p - (p * 0.05)))
        elif parcela == 2:
            print('O valor é R${:.2f}, e as parcelas ficaram 2X R${:.2f}'.format(p, (p / 2)))
        elif parcela >= 3:
            preco = p + (p * 0.2)
            print('O valor do produto será reajustado com 20% de juros, e o valor das parcelas'
                  '\n{}X R${:.2f}'.format(parcela, (preco / parcela)))
else:
    print("FORMA INVÁLIDA!!")
