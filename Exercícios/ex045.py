from random import choice
from time import sleep
print('Pedra, Papel ou Tesoura?')
j = str(input('Digite sua opção: ')).lower()
lista = ['pedra', 'papel', 'tesoura']
pc = (choice(lista))
print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PO!!')
if j == pc:
    print(pc)
    print('EMPATE')
elif j == 'pedra' and pc == 'tesoura' or j == 'tesoura' and pc == 'papel' or j == 'papel' and pc == 'pedra':
    print(pc)
    print('VC GANHOU!')
elif pc == 'pedra' and j == 'tesoura' or pc == 'tesoura' and j == 'papel' or pc == 'papel' and j == 'pedra':
    print(pc)
    print('VC PERDEU')
else:
    print('\033[31mRESPOSTA INVÁLIDA')
