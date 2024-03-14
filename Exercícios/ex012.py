ap = str(input('Qual o aparelho que você quer comprar? '))
p = float(input('Entendi...Qual o valor dele? '))

p1 = p - (p * 0.05)

print('\nNossa loja está com uma promoção de 5% de desconto para todos os produtos\n'
      'O produto que você escolheu: {}\n'
      'Está com um preço inicial de R${} reais\n'
      'Em nossa promoção o preço cairá para R${:.6} reais'.format(ap, p, p1))
