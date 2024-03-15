d = int(input('Quantos dias o carro foi alugado? '))
k = float(input('Qual a kilometragem rodada? '))
# Equação
p = (d * 60) + (k * 0.15)

print('O valor à pagar é: R${:.2f} reais'.format(p))
